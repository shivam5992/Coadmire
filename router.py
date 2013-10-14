from flask import *
from functools import wraps
from pymongo import MongoClient

client = MongoClient()
db = client.coadtest
collection = db.level1

app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/')
def index():
	return render_template('index.html',collection =  collection)

if __name__ == '__main__' :
	app.run(debug=True)

