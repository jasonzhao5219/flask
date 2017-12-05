from flask import Flask, render_template, request, redirect,flash,url_for
from datetime import datetime
import re
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
REGEX_email=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Upper=re.compile(r'^[A-Z]+[0-9]')

@app.route('/',methods=['post','get'])
def whatever1():
	return render_template('rform.html')

@app.route('/process', methods=['post'])
def vali():
	error=False
	if len(request.form['first_name']) < 1 or len(request.form['last_name'])<1 or len(request.form['email'])<1 or len(request.form['password'])<1 or len(request.form['email'])<1 or len(request.form['comfirm_password'])<1:
		flash("all input should be valid", "empty input is invalid")
		error=True
	if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
		flash("last name and first name can not contain numbers","name")
		error=True
	if len(request.form['password'])<1:
		flash("the character length is less than 8","password")
		error=True
	if request.form['password']!=request.form['comfirm_password']:
		flash("the password you input is not as same as before","password2")
		error=True
	if not REGEX_email.match(request.form['email']):
		flash("email is not valid","email")
		error=True
	if not Upper.match(request.form['password']) :
		flash("password should have at least one uppercase letter !","ninja level thing: ")
		error=True
	"""if  request.form['datetime'] != datetime.strptime(request.form['datetime'], "%Y-%m-%d").strftime('%Y-%m-%d'): 
		flash("Hacthon level thing: the data and time you input is invalid!","123")
		error=True"""
	if error:
		return redirect('/')
	if not error:
		return redirect('/ss')
@app.route('/ss')
def ss():
	return render_template('succ.html')



app.run(debug=True)