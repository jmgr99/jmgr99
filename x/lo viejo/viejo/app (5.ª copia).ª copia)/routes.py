from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import copy



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	email = request.form['email']
	name = request.form['name']

	if name and email:
		newName = name[::-1]

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)
