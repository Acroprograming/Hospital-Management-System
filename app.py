#pythgon flask app

from flask import Flask, request, render_template, url_for
import json
import os.path
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
#app.config('SQLALCHEMY_TRACK_MODIFICATIONS')=False 
#app.config['SQLALCHEMY_DATABASE_URI']=
@app.route('/',methods=['GET','POST'])
def welcome():
	name=''
	pas=''
	if request.method=='POST' and 'username' in request.form:
		name=request.form.get('username')
		if name=="Admin":
			pas=request.form.get("password")
			if pas=="Admin":
				return render_template('update_patient.html')

	return render_template('index.html',name=name)

@app.route('/updatepatient')
def update_patient():
	return render_template('update_patient.html')

app.run()