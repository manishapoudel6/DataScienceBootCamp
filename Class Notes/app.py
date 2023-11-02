from flask import Flask, request

#instance of flask application
app = Flask("MyApp")
#app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello, Everyone! How are you all?</p>"

@app.route("/hi")
def viewfun():
	return "<p>All Good?</p>" #p is for paragrapgh


@app.route("/hi/hello")
def viewfunc():
	return "<h1>Alright</h1>" #h1 is for heading text

@app.route("/add", methods = ['POST'])
def addition():
	a=request.json['a']
	b=request.json['b']
	return {'sum':int(a)+int(b)}

@app.route("/sub", methods = ['POST'])
def subtraction():
	a=request.json['a']
	b=request.json['b']
	return {'subtraction':int(a)-int(b)}

@app.route("/div", methods = ['POST'])
def division():
	a=request.json['a']
	b=request.json['b']
	return {'division':int(a)/int(b)}

@app.route("/mul", methods = ['POST'])
def multiplication():
	a=request.json['a']
	b=request.json['b']
	return {'multiplication':int(a)*int(b)}



if __name__ == '__main__':
	app.run()
