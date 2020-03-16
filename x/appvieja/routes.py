from app import app
from flask import Flask, render_template, request, url_for, escape
import copy

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/index')
#def index():
#    user = {'username': 'Miguel'}
#    posts = [
#        {
#            'author': {'username': 'John'},
#            'body': 'Beautiful day in Portland!'
#        },
#        {
#            'author': {'username': 'Susan'},
#            'body': 'The Avengers movie was so cool!'
#        }
#    ]
#    return render_template('index.html', title='Home', user=user, posts=posts)
#
@app.route('/quiz', methods=['POST','GET'])
def quiz():


    if request.method == 'POST':
        response = request.form['response']
        answer = "Is"
        return render_template('answer.html', response=response, answer=answer)

    else:
        return render_template("newquiz.html")
