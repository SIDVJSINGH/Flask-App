from flask import render_template, request
from application.all_questions import questions_list
from application import app


@app.route("/", methods = ['GET'])
def home():
    return render_template("index.html", questions_list=questions_list)


@app.route("/answers", methods=['GET', 'POST'])
def answer():
    results: int = 0
    sel: list = ["Selected"]
    cor: list = ["Correct"]
    score: list = ["Score Board"]
    for question in questions_list:
        q_id = str(question.qestion_no)
        selected = request.form[q_id]
        correct = question.get_right()
        sel.append(selected)
        cor.append(correct)
        if selected == correct:
            results = results + 1
    score.append(results)
    score.append(cor)
    score.append(sel)
    return score
