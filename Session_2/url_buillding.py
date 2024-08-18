from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

@app.route("/pass/<name>/<int:num>")
def passed(name,num):
    return f"Congrats {name.title()} , you have passed with {num} marks ."

@app.route("/fail/<name>/<int:num>")
def failed(name,num):
    return f"Sorry {name.title()} , you have failed with {num} marks ."

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        return redirect(url_for("failed",name=name,num=num))
    else:
        return redirect(url_for("passed",name=name,num=num))


if __name__=="__main__":
    app.run(debug=True)