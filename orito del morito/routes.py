from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import json



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	object = request.form['object']
	objectb = request.form['object']
	objectx = 'sahih'
	objecty = 'hata'

#	if object == 'x':
#		objecta = 'sahih'

#	if object != 'x':
#		objecta = 'hata'


#	if objectb != 'y':
#		objectx = 'hata'

	return jsonify(object=objectx,
                   objectb=objecty)

#	return jsonify ( {'object' : objecty} )

if __name__ == '__main__':
	app.run(debug=True)
