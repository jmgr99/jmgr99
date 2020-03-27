from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import json, random

root = "درس"
verb = "x"
testroot ='فعل'

listedroot = list(root)
rad3 = (listedroot.pop(2))
rad2 = (listedroot.pop(1))
rad1 = (listedroot.pop(0))




str1 = ""
fatha = b'\xD9\x8E'.decode('utf-8')
damma = b'\xD9\x8F'.decode('utf-8')
ksra = b'\xD9\x90'.decode('utf-8')
sukun = b'\xD9\x92'.decode('utf-8')
time = f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}"



def conjugate(root,time,person):
	listedroot = list(root)
	rad3 = (listedroot.pop(2))
	rad2 = (listedroot.pop(1))
	rad1 = (listedroot.pop(0))
	if time == 'past':
		I = 'تُ'
		youm = 'تَ'
		youf = 'تِ'
		youtwo = 'تُمَا'
		she = 'تْ'
		theytwomasc = "ا"
		theytwofem = "تَا"
		we = 'نَا'
		youmascpl = 'تُم'
		youfempl = 'ت'
		theymasc = 'وا'
		theyfem = 'نَ'

		if person == 'Isg':
			a1 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{sukun}{I}")
			return a1

		elif person == 'IIsgmasc':
			a2 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{sukun}{youm}")
			return a2

		elif person == 'IIsgfem':
			a3 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{sukun}{youf}")
			return a3

		elif person == 'IIdual':
			a4 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{sukun}{youtwo}")
			return a4

		elif person == 'IIIsgmasc':
			a5 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}")
			return a5

		elif person == 'IIIsgfem':
			a6 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}{she}")
			return a6
		elif person == 'IIIdualmasc':
			a7 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}{theytwomasc}")
			return a7

		elif person == 'IIIdualfem':
			a8 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}{theytwofem}")
			return a8

		elif person == 'Ipl':
			a9 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{sukun}{we}")
			return a9

		elif person == 'IIplmasc':
			a10 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youmascpl}")
			return a10

		elif person == 'IIplfem':
			a11 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youfempl}")
			return a11

		elif person == 'IIIplmasc':
			a12 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{damma}{theymasc}")
			return a12

		elif person == 'IIIplfem':
			a13 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{theyfem}")
			return a13

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/formI/index')
def indexformi():
	pastIIIsgmasc = conjugate (testroot,"past",'IIIsgmasc')
	presentIIIsgmasc = 'ي'
	root = testroot
	form = 'Form I'
	wasan = conjugate (testroot,"past",'IIIsgmasc')

	pastIsg = conjugate (testroot,"past",'Isg')
	pastIIsgmasc = conjugate (testroot,"past",'IIsgmasc')
	pastIIsgfem = conjugate (testroot,"past",'IIsgfem')
	pastIIdual = conjugate (testroot,"past",'IIdual')
#	pastIIIsgmasc = conjugate (testroot,"past",'IIIsgmasc')
	pastIIIsgfem = conjugate (testroot,"past",'IIIsgfem')
	pastIIIdualmasc = conjugate (testroot,"past",'IIIdualmasc')
	pastIIIdualfem = conjugate (testroot,"past",'IIIdualfem')
	pastIpl = conjugate (testroot,"past",'Ipl')
	pastIIplmasc = conjugate (testroot,"past",'IIplmasc')
	pastIIplfem = conjugate (testroot,"past",'IIplfem')
	pastIIIplmasc = conjugate (testroot,"past",'IIIplmasc')
	pastIIIplfem = conjugate (testroot,"past",'IIIplfem')
	return render_template('indexFormI.html',
							pastIIIsgmasc=pastIIIsgmasc,
							presentIIIsgmasc=presentIIIsgmasc,
							root=root,
							form=form,
							wasan=wasan,
							pastIsg=pastIsg,
							pastIIsgmasc=pastIIsgmasc,
							pastIIsgfem=pastIIsgfem,
							pastIIdual=pastIIdual,
#							pastIIIsgmasc=pastIIIsgmasc,
							pastIIIsgfem=pastIIIsgfem,
							pastIIIdualmasc=pastIIIdualmasc,
							pastIIIdualfem=pastIIIdualfem,
							pastIpl=pastIpl,
							pastIIplmasc=pastIIplmasc,
							pastIIplfem=pastIIplfem,
							pastIIIplmasc=pastIIIplmasc,
							pastIIIplfem=pastIIIplfem,
							 )



@app.route('/formI/past')
def pastformi():
	pastIIIsgmasc = conjugate (testroot,"past",'IIIsgmasc')
	presentIIIsgmasc = 'ي'
	root = testroot
	form = 'Form I'
	wasan = conjugate (testroot,"past",'IIIsgmasc')
	a1 = conjugate (root,"past",'Isg')
	a2 = conjugate (root,'past','IIsgmasc')
	a3 = conjugate (root,'past','IIsgfem')
	a4 = conjugate (testroot,"past",'IIdual')
	a5 = conjugate (testroot,"past",'IIIsgmasc')
	a6 = conjugate (testroot,"past",'IIIsgfem')
	a7 = conjugate (testroot,"past",'IIIdualmasc')
	a8 = conjugate (testroot,"past",'IIIdualfem')
	a9 = conjugate (testroot,"past",'Ipl')
	a10 = conjugate (testroot,"past",'IIplmasc')
	a11  = conjugate (testroot,"past",'IIplfem')
	a12  = conjugate (testroot,"past",'IIIplmasc')
	a13  = conjugate (testroot,"past",'IIIplfem')
	return render_template('formIpast.html',
										pastIIIsgmasc=pastIIIsgmasc,
										presentIIIsgmasc=presentIIIsgmasc,
										root=root,
										form=form,
										wasan=wasan,
										a1=a1,
										a2=a2,
										a3=a3,
										a4=a4,
										a5=a5,
										a6=a6,
										a7=a7,
										a8=a8,
										a9=a9,
										a10=a10,
										a11=a11,
										a12=a12,
										a13=a13,
										)

@app.route('/process', methods=['POST'])
def process():

	a1 = request.form['a1']
	a2 = request.form['a2']
	a3 = request.form['a3']
	a4 = request.form['a4']
	a5 = request.form['a5']
	a6 = request.form['a6']
	a7 = request.form['a7']
	a8 = request.form['a8']
	a9 = request.form['a9']
	a10 = request.form['a10']
	a11 = request.form['a11']
	a12 = request.form['a12']
	a13 = request.form['a13']



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
	r11 = request.form['r11']
	r12 = request.form['r12']
	r13 = request.form['r13']



	if r1 == a1:
		sol1 = 'صحيح'

	if r1 != a1:
		sol1 = 'خطأ'

	if r2 == a2:
		sol2 = 'صحيح'

	if r2 != a2:
		sol2 = 'خطأ'

	if r3 == a3:
		sol3 = 'صحيح'

	if r3 != a3:
		sol3 = 'خطأ'

	if r4 == a4:
		sol4 = 'صحيح'

	if r4 != a4:
		sol4 = 'خطأ'

	if r5 == a5:
		sol5 = 'صحيح'

	if r5 != a5:
		sol5 = 'خطأ'
	if r6 == a6:
		sol6 = 'صحيح'
	if r6 != a6:
		sol6 = 'خطأ'
	if r7 == a7:
		sol7 = 'صحيح'
	if r7 != a7:
		sol7 = 'خطأ'

	if r8 == a8:
		sol8 = 'صحيح'
	if r8 != a8:
		sol8 = 'خطأ'

	if r9 == a9:
		sol9 = 'صحيح'
	if r9 != a9:
		sol9 = 'خطأ'

	if r10 == a10:
		sol10 = 'صحيح'
	if r10 != a10:
		sol10 = 'خطأ'

	if r11 == a11:
		sol11 = 'صحيح'
	if r11 != a11:
		sol11 = 'خطأ'

	if r12 == a12:
		sol12 = 'صحيح'
	if r12 != a12:
		sol12 = 'خطأ'

	if r13 == a13:
		sol13 = 'صحيح'
	if r13 != a13:
		sol13 = 'خطأ'

	return jsonify(r1=sol1,
                    r2=sol2,
                    r3=sol3,
                    r4=sol4,
                    r5=sol5,
                    r6=sol6,
                    r7=sol7,
                    r8=sol8,
                    r9=sol9,
                    r10=sol10,
					r11=sol11,
					r12=sol12,
					r13=sol13,
                    )


if __name__ == '__main__':
	app.run(debug=True)
