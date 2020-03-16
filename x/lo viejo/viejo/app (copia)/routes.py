from app import app
from flask import Flask, render_template, request, url_for, escape, jsonify
import copy



@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])


if __name__ == '__main__':
	app.run(debug=True)
