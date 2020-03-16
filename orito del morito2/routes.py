from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import json



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	object = request.form['object']
	objectb = request.form['objectb']

	if object == 'x':
		objectx = 'sahih'

	if object != 'x':
		objectx = 'hata'

	if objectb == 'y':
		  objecty = 'sahih'

	if objectb != 'y':
		  objecty = 'hata'

	return jsonify(object=objectx,
				   objectb=objecty)

#	return jsonify ( {'object' : objecty} )

if __name__ == '__main__':
	app.run(debug=True)
