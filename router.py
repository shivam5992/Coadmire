from flask import *
from functools import wraps

app = Flask(__name__)
app.secret_key = 'shivam_bansal'

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__' :
	app.run(debug=True)

