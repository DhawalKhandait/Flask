from flask import Flask

#  create the flask app
app=Flask(__name__)

@app.route("/")
def home():
    return"Welcome to page" 

@app.route("/about")
def about():
    return "About page is here"


if __name__ == "__main__":
	app.run(debug=True)    