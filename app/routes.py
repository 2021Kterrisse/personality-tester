from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template ("index.html")

@app.route('/results', methods = ["get", "post"])
def results():

    info = dict(request.form)
    print(info)

    question1 = info["question1"]
    question2 = info["question2"]
    question3 = info["question3"]
    question4 = info["question4"]
    question5 = info["question5"]

    output = model.question(question1, question2, question3, question4, question5)
    print (output)

    return render_template ('Results.html', question = output)
