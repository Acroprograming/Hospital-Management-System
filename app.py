#pythgon flask app

from flask import Flask, request, render_template, url_for, redirect
import json
import os.path
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
#app.config('SQLALCHEMY_TRACK_MODIFICATIONS')=False 
#app.config['SQLALCHEMY_DATABASE_URI']=
@app.route('/',methods=['GET','POST'])
def welcome():
	if request.method=="POST":
		name=request.form['user_id']
		passw=request.form['password']
		if name=="Admin" and passw=="Admin":
			return redirect(url_for('update_patient'))
		else:
			render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/updatepatient')
def update_patient():
	return render_template('update.html')


app.run()