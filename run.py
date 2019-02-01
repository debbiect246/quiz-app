import os
import json
from flask import Flask, render_template, request, flash, redirect, session, url_for

from random import shuffle

app = Flask(__name__) 
app.secret_key = 'some_secret'

def readfile():
    with open("data/quizdata.json", "r") as read_file:
        data = json.load(read_file)
        return data

@app.route("/", methods = ["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

        if "username" in session:
            return redirect(url_for("quiz", username=session["username"]))
        
    else:
        return render_template("index.html")
    
@app.route("/<username>", methods = ["GET", "POST"])
def user(username):
    """Display welcome message"""
    if request.method == "POST":
        return'<h1>Welcome ' + username + ' to the quiz</h1>'
    return render_template("index.html")
 
def logout():
    if session:
        session.clear()
        flash("You have logged out")
        return render_template("index.html")
     
     

@app.route('/quiz/<username>', methods=["GET", "POST"])

def quiz(username):
    
    data=readfile()
    shuffle(data)
    if username==session["username"]:
        if request.method == 'Post':
            
            return render_template("quiz.html",page_title="Quiz", data=data, username=username)
        
        else: 
            #return a template with the riddles
            return render_template("quiz.html",page_title="Quiz", data=data, username=username)
    else:
        return render_template("quiz.html")
   


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")


@app.route('/feedback', methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("feedback.html", page_title="Feedback")
    


@app.route('/newquestions', methods=["GET", "POST"])
def newquestions():
    if request.method == "POST":
        flash("Thanks {}, we have received your question".format(
            request.form["name"]
        ))
    return render_template("newquestions.html", page_title="New questions")
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)