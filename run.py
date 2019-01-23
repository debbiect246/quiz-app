import os
import json
from flask import Flask, render_template, request, flash
from random import shuffle

app = Flask(__name__) 
app.secret_key = 'some_secret'

with open("data/quizdata.json", "r") as read_file:
     data = json.load(read_file)

@app.route('/')
def index():
    return render_template("index.html", page_title="Home")


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    qw = data 
    return render_template("quiz.html", page_title="Quiz", data = qw)
   


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
    return render_template("newquestions.html", page_title="Newquestions")
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

            