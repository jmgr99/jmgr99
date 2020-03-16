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
    a2 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youm}")
    a3 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youf}")
    a4 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}")
    a5 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}{she}")
    a6 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{we}")
    a7 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youmascpl}")
    a8 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youfempl}")
    a9 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{damma}{theymasc}")
    a10= str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{theyfem}")



@app.route('/')
def index():

	return render_template('form.html', a1=a1, a2=a2, a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,a10=a10, root=root, time=time,)

@app.route('/process', methods=['POST'])
def process():

	r1 = request.form['r1']
	r2 = request.form['r2']
	r3 = request.form['r3']
	r4 = request.form['r4']
	r5 = request.form['r5']
	r6 = request.form['r6']
	r7 = request.form['r7']
	r8 = request.form['r8']
	r9 = request.form['r9']
	r10 = request.form['r10']

	if r1 == a1:
		sol1 = 'sahih'

	if r1 != a1:
		sol1 = 'hata'

	if r2 == a2:
		sol2 = 'sahih'

	if r2 != a2:
		sol2 = 'hata'

	if r3 == a3:
		sol3 = 'sahih'

	if r3 != a3:
		sol3 = 'hata'

	if r4 == a4:
		sol4 = 'sahih'

	if r4 != a4:
		sol4 = 'hata'

	if r5 == a5:
		sol5 = 'sahih'

	if r5 != a5:
		sol5 = 'hata'

	if r6 == a6:
		sol6 = 'sahih'

	if r6 != a6:
		sol6 = 'hata'

	if r7 == a7:
		sol7 = 'sahih'

	if r7 != a7:
		sol7 = 'hata'

	if r8 == a8:
		sol8 = 'sahih'

	if r8 != a8:
		sol8 = 'hata'

	if r9 == a9:
		sol9 = 'sahih'

	if r9 != a9:
		sol9 = 'hata'

	if r10 == a10:
		sol10 = 'sahih'

	if r10 != a10:
		sol10 = 'hata'

	return jsonify(r1=sol1,
                    r2=sol2,
                    r3=sol3,
                    r4=sol4,
                    r5=sol5,
                    r6=sol6,
                    r7=sol7,
                    r8=sol8,
                    r9=sol9,
                    r10=sol10
                    )
    #r3=sol3,
    #r4=sol4,
    #r5=sol5,
    #r6=sol6,
    #r7=sol7,
    #r8=sol8,
    #r9=sol9,
    #r10=sol10,)

#	return jsonify ( {'object' : objecty} )

if __name__ == '__main__':
	app.run(debug=True)
