import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/newquestions')
def newquestions():
    return render_template("newquestions.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            