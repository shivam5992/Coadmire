from flask import *
from functools import wraps
from pymongo import MongoClient
import random

client = MongoClient()
db = client.coadtest

level_id = 0
count = 0

app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/',methods=['GET','POST'])
def index(): 
	resp = None
	global level_id
	global count 

	# previous question check
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
		else:
			resp = 'you response was not correct'
			if level_id != 0:
				level_id -= 1
	
	count += 1
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