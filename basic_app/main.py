from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
	return "Method Used: %s" % request.method

@app.route('/bacon', methods =['GET', 'POST'])
def bacon():
	if request.method == 'POST':
		return 'You are using POST'
	return  "You are probably using GET"


@app.route('/tuna')
def tuna():
	return'<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
	return "<h2>Hey there %s</h2>" % username


@app.route('/post/<int:post_id>')
def employee(post_id):
	return "<h2>Post ID %s</h2>" % post_id

if __name__ == "__main__":
	app.run(debug=True)


#default data type is string, others you have to specify