from flask import *
from functools import wraps
from pymongo import MongoClient
import random

client = MongoClient()
db = client.coadtest

level_id = 0
count = 0
max_questions = 30
u_res = 0
positive_marks_for_question = 4
negative_marks_for_question = 1

app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/',methods=['GET','POST'])
def index(): 
	resp = None
	global level_id
	global count 
	global max_questions
	global u_res

	# previous question check
	if request.method == 'POST':
		#question check
		level = "level" + str(level_id)
		Q = request.form['question']
		pcollection = db[level]
		pdoc = pcollection.find_one({ 'question' : Q })
		A = pdoc['answer']
		if request.form['ques_response'] == A:
			resp = 'you response was correct'
			if level_id != 9:
				level_id += 1
			u_res += positive_marks_for_question
		else:
			resp = 'you response was not correct'
			if level_id != 0:
				level_id -= 1
			u_res -= negative_marks_for_question

		#store result
		user_level = level
		user_question = request.form['question']
		user_response = request.form['ques_response']
		user_answer = pdoc['answer']
		user_result = u_res
		user_time_spent = 0
		#change collection name for particular user
		collection = db.userResponse
		result_doc ={
		'question' : user_question,
		'answer' :   user_answer,
		'response' : user_response,
		'time':      user_time_spent,
		'level':	 user_level
		}
		collection.insert(result_doc)
		
		'''flash(user_level)
		flash(user_question)
		flash(user_response)
		flash(user_result)
		flash(user_time_spent)
		flash(user_answer)'''
	
	count += 1
	if count == max_questions+1:
		return render_template('finished.html')
	else:	
		flash(count)
		level = "level" + str(level_id)
		collection = db[level]
		Ques_id = random.randrange(1,5)
		doc = collection.find_one({ '_id' : Ques_id })
		return render_template('index.html',doc =  doc)

@app.route('/box')
def box():
	return render_template('box.html') 
	
if __name__ == '__main__' :
	app.run(debug=True)