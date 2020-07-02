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
		else:
			patient_details=db1.execute(
				'SELECT * FROM patient WHERE patient_id = ?', (patient_id,)
				).fetchall()
			print(5)
			print(patient_details)
			return render_template('pharmacist/view_patient.html',patients=patient_details)
	return render_template('pharmacist/view_patient.html')









