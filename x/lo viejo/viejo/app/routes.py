from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import copy



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	if name:
		return jsonify({'go' : 'go'})



if __name__ == '__main__':
	app.run(debug=True)
