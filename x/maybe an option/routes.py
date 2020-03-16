from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import json
root = "درس"
listedroot = list(root)
print(listedroot)
rad3 = (listedroot.pop(2))
rad2 = (listedroot.pop(1))
rad1 = (listedroot.pop(0))

str1 = ""
fatha = b'\xD9\x8E'.decode('utf-8')
damma = b'\xD9\x8F'.decode('utf-8')
ksra = b'\xD9\x90'.decode('utf-8')
time = f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}"


import random
#pronounslist = ['أنا', 'أنتَ', 'أنتِ', 'أنتما', , 'هي', 'أنتم', 'أنتن', 'نحن', 'هم', 'هن']
time = "past"
#include random list for time
#print(pronoun)

if time == "past":
    I = 'تُ'
    youm = 'تَ'
    youf = 'تِ'
    youtwo = 'تُمَا'
    #he =
    she = 'ت'
    we = 'نَا'
    youmascpl = 'تُم'
    youfempl = 'ت'
    theymasc = 'وا'
    theyfem = 'نَ'

    a1 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{I}")


@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	object = request.form['object']
	objectb = request.form['objectb']


	if object == a1:
		objectx = 'sahih'

	if object != a1:
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
