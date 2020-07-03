
import os
from flask import Flask
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .auth import login_required

from . import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # a simple page that says hello
    @app.route('/index')
    def index():
        return 'Hello, World!'

    

    @app.route('/add_patient', methods=('GET', 'POST'))
    @login_required
    def add_patient():
        if request.method == 'POST':
            patient_id = request.form['patient_id']
            patient_name = request.form['patient_name']
            patient_age = request.form['patient_age']
            date_of_addmision = request.form['date_of_addmision']
            type_of_room = request.form['type_of_room']
            address = request.form['address']
            state = request.form['state']
            city= request.form['city']
            db2=db.get_db()
            res=db2.execute('INSERT INTO patient(patient_id,patient_name,patient_age,date_of_admission,type_of_room,address,state,city,date_of_joining) VALUES (?,?,?,?,?,?,?,?,"9");',(patient_id,patient_name,patient_age,date_of_addmision,type_of_room,address,state,city))
            db2.commit()
            print(res)
            return redirect(url_for('view_patients'))
        return render_template('patient/add_patient.html')

    @app.route('/view_patients',methods=('GET', 'POST'))
    @login_required
    def view_patients():
        db3=db.get_db()
        plist=db3.execute('SELECT * FROM patient').fetchall()
        print("PList")
        print(plist)
        return render_template('patient/view_all_patients.html',patients=plist )

    @app.route('/delete_patient',methods=('GET', 'POST'))
    @login_required
    def delete_patient():
        if request.method=='POST': 
            patient_id=request.form['patient']
            if not patient_id:
                error="First search the patient you want to delete"
                flash(error)
            else:
                db3=db.get_db()
                db3.execute('Delete From patient where patient_id= ?',(patient_id,))
                redirect(url_for('view_patients'))
                db3.commit()
                flash("Patient Deleted Successfully")
            return render_template('patient/delete_patient.html')
        return render_template('patient/delete_patient.html')

    @app.route('/delete_patient_id',methods=('GET', 'POST'),endpoint="get_patient")
    def get_patient():
        if request.method == 'POST':
            patient_id = request.form['patient_id']
            db1=db.get_db()
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
                return render_template('patient/delete_patient.html',patients=patient_details)
        return render_template('pharmacist/view_patient.html')
    @app.route('/update_patient',methods=('GET', 'POST'))
    @login_required
    def update_patient():
        if request.method=='POST': 
            patient_id=request.form['patient']
            if not patient_id:
                error="First search the patient you want to delete"
                flash(error)
            else:
                patient_id=request.form['patient']
                patient_name = request.form['patient']
                patient_age = request.form['patient']
                date_of_admission = request.form['patient']
                type_of_room = request.form['patient']
                address = request.form['patient']
                state = request.form['patient']
                city= request.form['patient']
                db3=db.get_db()
                db3.execute('Update patient set patient_name=?,patient_age=?,date_of_admission=?,type_of_room=?,address=?,state=?,city=? where patient_id= ?',(patient_name,patient_age,date_of_admission,type_of_room,address,state,city,patient_id))
                redirect(url_for('view_patients'))
                db3.commit()
                flash("Patient Updated Successfully")
            return render_template('patient/update_patient.html')
        return render_template('patient/update_patient.html')
    
    @app.route('/update_patient_id',methods=('GET', 'POST'),endpoint="get_patient2")
    def get_patient2():
        if request.method == 'POST':
            patient_id = request.form['patient_id']
            db1=db.get_db()
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
                return render_template('patient/update_patient.html',patients=patient_details)
        return render_template('pharmacist/view_patient.html')

    db.init_app(app)

    from . import pharmacist
    app.register_blueprint(pharmacist.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
