from flask import Flask, request
import pickle
import numpy as np

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

@app.route("/iris", methods = ['POST'])
def classify():
	a=request.json['a']
	b=request.json['b']
	c=request.json['c']
	d=request.json['d']
	loaded_model = pickle.load(open('model.pkl','rb'))
	test = np.array([a,b,c,d]).reshape(1,-1)
	print(test.shape)
	print(loaded_model.predict(test))
	return {'prediction':str(loaded_model.predict(test)[0])}



if __name__ == '__main__':
	app.run()
