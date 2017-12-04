from flask import Flask, render_template, request, redirect,flash
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/',methods=['post','get'])
def submitaform():
	return render_template("dojosurverform.html")
@app.route('/process',methods=['POST'])
def getr():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!") 
	elif len(request.form['comment'])>12:
		flash("The length of Comment is too long!")
	

	else:
		flash("Success! Your name is {}".format(request.form['name']))
	return render_template("result.html",name=request.form["name"],location=request.form["location"],language=request.form["language"],comment=request.form["comment"])

app.run(debug=True)