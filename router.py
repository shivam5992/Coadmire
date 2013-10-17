from flask import *
from functools import wraps
from pymongo import MongoClient
import random

client = MongoClient()
db = client.coadtest

#set these variables
max_questions = 30
positive_marks_for_question = 4
negative_marks_for_question = 1

level_id = 0
count = 0
user_score_so_far = 0


app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/',methods=['GET','POST'])
def index(): 
	resp = None
	user_name = "shivam"
	user_id =  "10103475"
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
			resp = 'you response was correct'
			if level_id != 9:
				level_id += 1
			user_score_so_far += positive_marks_for_question
		else:
			resp = 'you response was not correct'
			if level_id != 0:
				level_id -= 1
			user_score_so_far -= negative_marks_for_question

		
		# store result for a particular user, store each question as docs
		userResponse = "ReponseOf"+user_name+user_id
		
		user_level = level
		user_question = request.form['question']
		user_answer = pdoc['answer']
		user_response = request.form['ques_response']
		user_result = user_score_so_far
		
		collection = db[userResponse]
		result_doc ={
		'userName' : user_name,
		'UserId'  : user_id,
		'level':	 user_level,
		'question' : user_question,
		'answer' :   user_answer,
		'response' : user_response,
		'score'  :   user_result
		}
		collection.insert(result_doc)
		
		
	
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
 
	
if __name__ == '__main__' :
	app.run(debug=True)