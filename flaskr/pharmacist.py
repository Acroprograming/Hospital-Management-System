from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from flaskr.auth import login_required

bp = Blueprint('pharmacist', __name__, url_prefix='/pharmacist')

@bp.route('/view_patient', methods=('GET', 'POST'))
@login_required
def view_patient():
	if request.method == 'POST':
		patient_id = request.form['patient_id']
		db1=get_db()
		error= None

		if not patient_id:
			error="patient_SSN_id is required"
			flash(error)
		else:
			patient_details=db1.execute(
				'SELECT * FROM patient WHERE patient_id = ?', (patient_id,)
				).fetchall()
			print(5)
			print(patient_details)
			return render_template('pharmacist/view_patient.html',patients=patient_details)
	return render_template('pharmacist/view_patient.html')

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
			return render_template('pharmacist/patient_info.html',patients=patient_details)
	return render_template('pharmacist/patient_info.html')


@bp.route('/show_medicines_issued', methods=('GET', 'POST'))
@login_required
def show_medicines_issued():
	if request.method == 'POST':
		patient_id = request.form['patient']
		db1=get_db()
		error= None
		if not patient_id:
			error="patient_SSN_id is required"
		else:
			medicines=db1.execute(
				'SELECT * FROM medicine INNER JOIN medicine_issued on medicine.medicine_id = medicine_issued.medicine_id WHERE patient_id = ?', (patient_id,)
				).fetchall()
		return render_template('pharmacist/show_medicines_issued.html',medicines=medicines)
	return 'Hello, World! Get'


@bp.route('/show_medicines', methods=('GET', 'POST'))
@login_required
def show_medicines():
	if request.method == 'POST':
		patient_id = request.form['patient_id']	
		db3=get_db()
		plist=db3.execute('SELECT * FROM medicine').fetchall()
		print("PList")
		print(plist)
		return render_template('pharmacist/show_medicines.html',medicines=plist,patient_id=patient_id )
	return render_template('pharmacist/show_medicines.html',medicines=plist )
@bp.route('/add_medicine', methods=('GET', 'POST'))
@login_required
def add_medicine():		
	if request.method == 'POST':
		medicine_id = request.form['medicine_id']
		medicine_name = request.form['medicine_name']
		medicine_rate = request.form['medicine_rate']
		available_quantity = request.form['available_quantity']
		db2=get_db()
		res=db2.execute('INSERT INTO medicine(medicine_id,medicine_name,rate,available_quantity) VALUES (?,?,?,?);',(medicine_id,medicine_name,medicine_rate,available_quantity))
		db2.commit()
		return redirect(url_for('pharmacist.patient_info'))
	return render_template('pharmacist/add_medicine.html')

@bp.route('/issue_medicine', methods=('GET', 'POST'))
@login_required
def issue_medicine():		
	if request.method == 'POST':
		medicine_id = request.form['medicine_id']
		patient_id = request.form['patient_id']
		quantity_issued = request.form['quantity_issued']
		available_quantity=request.form['available_quantity']
		db2=get_db()
		res=db2.execute('INSERT INTO medicine_issued(medicine_id,patient_id,quantity_issued) VALUES (?,?,?);',(medicine_id,patient_id,quantity_issued))
		db2.commit()
		db3=get_db()
		res=db3.execute('UPDATE medicine SET available_quantity= ? Where medicine_id= ?',(available_quantity,medicine_id))
		db3.commit()
		return "Medicine Issued to Patient please refresh the page to see the changes"
	return "Medicine can't be issued"









