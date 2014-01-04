'''
Router file : coadmire
Computerised Adaptability Test Platform built in python - flask and mongodb.

Author: Shivam Bansal 
Email: shivam5992@gmail.Com 
version: 0.3
'''


from flask import *
from functools import wraps
from pymongo import MongoClient
import random
import datetime

'''
Connection with mongodb server
'''
client = MongoClient()
db = client.coadmire


'''
Global Variables according to test.
'''
max_questions = 10	# maximum number of questoins in a test(Set it equal to maximul level)
positive_marks_for_question = 4	# positive marks for correct answer
negative_marks_for_question = 1 # negative marks for incorrect answer
duration = 1 	# duration of test in hours
max_level = 5	# highest level number
min_level = 1 	# lowest level number


'''
Do not alter the following variables
'''
level_id = 1
count = 0
user_score_so_far = 0
questions_asked_so_far = []

app = Flask(__name__)
app.secret_key = 'shivam_bansal'


'''
Login Actions 
'''
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args,**kwargs)
		else:
			flash('you need to login first')
			return redirect(url_for('login'))
	return wrap


@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	session.pop('yourname',None)
	return redirect (url_for('index'))


@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	global count
	global questions_asked_so_far 
	if request.method == 'POST':
		if request.form['password'] != 'admin':
			error = 'Invalid credientials, Please try again'
		else:
			session['logged_in'] = True
			session['yourname'] = request.form['username']
			count = 0
			level_id = 1
			questions_asked_so_far = []

			current_time = datetime.datetime.now()
			current_hour = current_time.strftime("%H")
			timer = int(current_hour)+duration
			send_time = current_time.strftime("%B %d, %Y ") + str(timer) + current_time.strftime(":%M:%S")
			
			strtime = 'var endDate = "' + send_time + '";//'
			new_content = ""
			jsfile = open("static/js/timer.js", "rt")
			for line in jsfile:
  				new_content = new_content + line.replace("var endDate =",strtime)
			jsfile.close()

			f = open('static/js/timer.js','w')
			f.write(new_content) 
			f.close() 

			return redirect(url_for('coadtest'))
	return render_template('login.html',error=error)


'''
Function which starts the test
'''
@app.route('/coadtest',methods=['GET','POST'])
@login_required
def coadtest(): 
	resp = None
	user_name = session['yourname']
	global level_id
	global count 
	global user_score_so_far

	if request.method == 'POST':
		level = "level" + str(level_id)
		Q = request.form['question']
		pcollection = db[level]
		pdoc = pcollection.find_one({ 'question' : Q })
		A = pdoc['answer']
		if request.form['ques_response'] == A:
			if level_id != max_level:
				level_id += 1
			user_score_so_far += positive_marks_for_question
		else:
			if request.form['ques_response'] != "not_answered":	
				if level_id != min_level:
					level_id -= 1
				user_score_so_far -= negative_marks_for_question

		
		'''
		Store result for a particular user, store each question as docs
		'''
		userResponse = "ResponseOf"+user_name	
		user_level = level
		user_question = request.form['question']
		user_answer = pdoc['answer']
		user_response = request.form['ques_response']
		user_result = user_score_so_far
		collection = db[userResponse]
		result_doc ={
		'userName' : user_name,
		'level':	 user_level,
		'question' : user_question,
		'answer' :   user_answer,
		'response' : user_response,
		'score'  :   user_result
		}
		collection.insert(result_doc)
		
	
	'''
	Ask a new question
	'''
	count += 1
	if count == max_questions+1:
		count = 0
		temp = "ResponseOf"+session['yourname']
		report = db[temp]
		return render_template('finished.html',report = report)
	else:	
		flash(count)
		level = "level" + str(level_id)
		collection = db[level]
		
		Ques_id = random.randrange(1,max_questions)
		this_ques = level+"."+str(Ques_id)

		while this_ques in questions_asked_so_far:
			Ques_id = random.randrange(1,max_questions)
			this_ques = level+"."+str(Ques_id)
			
		questions_asked_so_far.append(this_ques)
		doc = collection.find_one({ '_id' : Ques_id })
		return render_template('coadtest.html',doc =  doc)	


'''
Homepage
'''
@app.route('/')
def index():
	return render_template('index.html')	

'''
Instruction Page
'''
@app.route('/instructions')
def instructions():
	return render_template('instructions.html')

'''
Admin Panel
'''
@app.route('/admin',methods=['GET','POST'])
def admin():
	if request.method == 'POST':
		admin_quesion = request.form['question']
		admin_option1 = request.form['option1']
		admin_option2 = request.form['option2']
		admin_option3 = request.form['option3']
		admin_option4 = request.form['option4']
		admin_answer = request.form['answer']
		admin_level = request.form['level']
		admin_collection = db[admin_level]

		ida = admin_collection.count()
		admin_id = ida+1

		admin_doc ={
		'_id'		: 	admin_id,
		'question' 	: 	admin_quesion,
		'option1' 	: 	admin_option1,
		'option2' 	: 	admin_option2,
		'option3' 	: 	admin_option3,
		'option4' 	: 	admin_option4,
		'answer'	: 	admin_answer,
		'level'		:   admin_level,
		}

		admin_collection.insert(admin_doc)

	return render_template('admin.html')

'''
Start the server
'''		
if __name__ == '__main__' :
	app.run(debug=True)