from app import app
from flask import Flask, render_template, request, url_for, escape
import copy

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
    a10 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{theyfem}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST','GET'])
def quiz():


    if request.method == 'POST':
        a1 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{I}")
        a2 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youm}")
        a3 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youf}")
        a4 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}")
        a5 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{fatha}{she}")
        a6 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{we}")
        a7 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youmascpl}")
        a8 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{youfempl}")
        a9 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{damma}{theymasc}")
        a10 = str1.join(f"{rad1}{fatha}{rad2}{fatha}{rad3}{theyfem}")


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

        right = "green"
        wrong = "red"
        if a1 == r1:
            c1 = right
        else:
            r1 = "خطأ"
            c1 = wrong





        return render_template('newanswer.html', c1=c1, r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6, r7=r7, r8=r8, r9=r9, r10=r10, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9, a10=a10)

    else:
        return render_template("newquiz.html")
