from flask import Flask, render_template, request, redirect,session
import random
import time

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def getforminfo():

	session['gold']=0
	session['counter']=0
	session['x']=""
	session['y']=""
	session['z']=""
	session['casino']=""
	
	return render_template('index.html')

@app.route('/process_money',methods=['post'])
def whatever():
	session['place']=request.form['building']
	session['counter']+=1
	casino=" "
	x=" "
	y=" "
	z=" "
	print session['place']

	
	if session['place']=="farm":
		session['gold']=random.randrange(10, 21)
		x="Earned {} gold from the {}!  ".format(session['gold'],session['place'])
		x=x+time.ctime()
	if session['place']=="cave":
		session['gold']=random.randrange(5, 11)
		y="Earned {} gold from the {}!  ".format(session['gold'],session['place'])
		y=y+time.ctime()

	if session['place']=="house":
		session['gold']=random.randrange(2, 6)
		z="Earned {} gold from the {}!  ".format(session['gold'],session['place'])
		z=z+time.ctime()
	if session['place']=="casino":
		session['gold']=random.randrange(-50, 51)
		if session['gold']>=0:
			casino="You enter a casino and win {} gold from the {}!  ".format(session['gold'],session['place'])
		else:
			casino="You enter a casino and Lost {} gold from the {}!  ".format(-session['gold'],session['place'])
	
		
	
	session['x']=session['x']+x+" "
	session['y']+=y
	session['z']+=z
	session['casino']+=casino
	return render_template('index.html',logging4=session['casino'],x=session['x'],y=session['y'],z=session['z'])

app.run(debug=True)