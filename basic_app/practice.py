from flask import flask

app = Flask(__name__)

@app.route("/SHOPCUPCAKE/<user>")
def x(user):
	return x