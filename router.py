from flask import *
from functools import wraps
from pymongo import MongoClient
import random

client = MongoClient()
db = client.coadtest

level_id = 1
flag = "same"
count = 0

app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/',methods=['GET','POST'])
def index(): 
	resp = None
	global flag
	global level_id
	global count 
	level = "level1"

	if flag == "increased":
		level = "level" + str(level_id-1)
	elif flag == "decreased":
		level = "level" + str(level_id+1)
	else:
		level = "level" + str(level_id)	
	
	# previous question check
	if request.method == 'POST':
		Q = request.form['question']
		pcollection = db[level]
		pdoc = pcollection.find_one({ 'question' : Q })
		flash(pdoc['answer'])

		if request.form['ques_response'] == pdoc['answer']:
			resp = 'you response was correct'
			if level_id < 3:
				level_id += 1
				flag = "increased"
		else:
			resp = 'you response was not correct'
			if level_id > 1:
				level_id -= 1
				flag = "decreased"

	count += 1
	flash(count)
	# New level accn to new levelid,random ques from that level and displayed on screen.
	level = "level" + str(level_id)
	collection = db[level]
	Ques_id = random.randrange(1,5)
	doc = collection.find_one({ '_id' : Ques_id })
	return render_template('index.html',resp = resp,doc =  doc)
	
if __name__ == '__main__' :
	app.run(debug=True)