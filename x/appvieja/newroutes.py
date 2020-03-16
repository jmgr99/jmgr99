from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import json



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

#	object = request.form['object']
#	objectb = request.form['objectb']
	objectx = 'sahih'
	objecty = 'hata'
	jsonresponse = jsonify(object=objectx,
                   		  objectb=objecty)
	return jsonresponse



	#dict = json.dumps(appDict)
	#return dict
#	if object == 'x':
#		objecta = 'sahih'

#	if object != 'x':
#		objecta = 'hata'


#	if objectb != 'y':
#		objectx = 'hata'

#	answers = [{'object':objecty}]
	#return jsonify({'object':objecty})
	#return jsonify ( {'object' : objecty} )

if __name__ == '__main__':
	app.run(debug=True)
