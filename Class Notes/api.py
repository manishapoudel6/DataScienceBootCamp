from flask import Flask

#instance of flask application
app = Flask("MyApp")
#app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello, Everyone! How are you all?</p>"

@app.route("/hi")
def viewfun():
	return "<p>All Good?</p>" #p is for paragrapgh


@app.route("/hello")
def viewfunc():
	return "<h1>Alright</h1>" #h1 is for heading text



if __name__ == '__main__':
	app.run()



