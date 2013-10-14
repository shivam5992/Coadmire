from flask import *
from functools import wraps
from pymongo import MongoClient
import random

client = MongoClient()
db = client.coadtest
level_id = 1

app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/',methods=['GET','POST'])
def index(): 
	resp = None

	level_id = 1

	#level = "level" + str(level_id)
	collection = db.level1
	
	Ques_id = random.randrange(1,6)
	doc = collection.find_one({ '_id' : Ques_id })

	if request.method == 'POST':
		if request.form['ques'] == doc['answer']:
			resp = 'you response is correct'
			level_id += 1
		else:
			resp = 'you response is not correct'
			# level_id -= 1
	return render_template('index.html',resp = resp,doc =  doc)
	
if __name__ == '__main__' :
	app.run(debug=True)

