from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from flaskr.auth import login_required

bp = Blueprint('diagnostics', __name__, url_prefix='/diagnostics')

@bp.route('/patient_info', methods=('GET', 'POST'))
@login_required
def patient_info():
	if request.method == 'POST':
		patient_id = request.form['patient_id']
		db1=get_db()
		error= None

		if not patient_id:
			error="patient_SSN_id is required"
		else:
			patient_details=db1.execute(
				'SELECT * FROM patient WHERE patient_id = ?', (patient_id,)
				).fetchall()
			print(5)
			print(patient_details)
			return render_template('diagnostics/patient_info.html',patients=patient_details)
	return render_template('diagnostics/patient_info.html')

@bp.route('/add_diagnostics', methods=('GET', 'POST'))
@login_required
def add_diagnostics():		
	if request.method == 'POST':
		diagnostics_id = request.form['diagnostics_id']
		diagnostics_name = request.form['diagnostics_name']
		diagnostics_amount = request.form['diagnostics_amount']
		
		db2=get_db()
		res=db2.execute('INSERT INTO diagnostics(diagnostic_id,name_of_test,amount) VALUES (?,?,?);',(diagnostics_id,diagnostics_name,diagnostics_amount))
		db2.commit()
		return redirect(url_for('diagnostics.patient_info'))
	return render_template('diagnostics/add_diagnostics.html')

@bp.route('/show_diagnostics', methods=('GET', 'POST'))
@login_required
def show_diagnostics():
	if request.method == 'POST':
		patient_id = request.form['patient_id']	
		db3=get_db()
		plist=db3.execute('SELECT * FROM diagnostics').fetchall()
		print("PList")
		print(plist)
		return render_template('diagnostics/show_diagnostics.html',diagnostics=plist,patient_id=patient_id)
	return render_template('diagnostics/show_diagnostics.html',diagnostics=plist,patient_id=patient_id)

@bp.route('/issue_diagnostics', methods=('GET', 'POST'))
@login_required
def issue_diagnostics():		
	if request.method == 'POST':
		diagnostic_id = request.form['diagnostic_id']
		patient_id = request.form['patient_id']
		db2=get_db()
		res=db2.execute('INSERT INTO diagnostics_conducted(diagnostic_id,patient_id) VALUES (?,?);',(diagnostic_id,patient_id))
		db2.commit()
		return "diagnostic test assigned to patient please refresh the page to see the changes"
	return "diagnostics can't be Added"

@bp.route('/diagnostics_conducted', methods=('GET', 'POST'))
@login_required
def diagnostics_conducted():
	if request.method == 'POST':
		patient_id = request.form['patient']
		db1=get_db()
		error= None
		if not patient_id:
			error="patient_SSN_id is required"
		else:
			diagnostics=db1.execute(
				'SELECT * FROM diagnostics INNER JOIN diagnostics_conducted on diagnostics.diagnostic_id = diagnostics_conducted.diagnostic_id WHERE patient_id = ?', (patient_id,)
				).fetchall()
		return render_template('diagnostics/diagnostics_conducted.html',diagnostics=diagnostics)
	return 'Hello, World! Get'
