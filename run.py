import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/quiz')
def quiz():
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
    


@app.route('/newquestions')
def newquestions():
    return render_template("newquestions.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

            