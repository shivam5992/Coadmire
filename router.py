from flask import *
from functools import wraps
from pymongo import MongoClient

client = MongoClient()
db = client.coadtest

collection = db.level1

app = Flask(__name__)
app.secret_key = 'shivam_bansal'


@app.route('/',methods=['GET','POST'])
def index(): 
	error = None
	if request.method == 'POST':
		if request.form['ques'] == '21':
			error = 'you response is correct'
		else:
			error = 'you response is not correct'
	return render_template('index.html',error=error,collection =  collection)
	
if __name__ == '__main__' :
	app.run(debug=True)

