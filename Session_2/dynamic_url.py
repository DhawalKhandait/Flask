from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

@app.route("/about/<name>")
def about(name):
    return f"Welcome {name.title()} ."
    

if __name__=="__main__":
    app.run(debug=True)
