from flask import Flask , redirect , url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

@app.route("/pass")
def passed():
    return f"Congratulation you have passed"


@app.route("/fail")
def failed():
    return f"Sorry you have fail"


@app.route("/score/<int:num>")
def score(num):
    if num>30:
        return redirect(url_for("passed"))
    else :
        return redirect(url_for("failed"))    

if __name__=="__main__":
    app.run(debug=True)