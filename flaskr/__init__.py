import os
from flask import Flask
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

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

    @app.route('/login', methods=('GET', 'POST'))
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            db1 = db.get_db()
            error = None
            user = db1.execute(
                'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()

            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user['password'], password):
                error = 'Incorrect password.'

            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('index'))

            flash(error)

        return render_template('login.html')

    @app.route('/add_patient',methods=["GET","POST"])
    def add_patient():
        if request.method=="POST":
            pid=request.form['patient_SSN_Id']
            pname=request.form['Patient_Name']
            page=request.form['Patient_Age']
            doa=request.form['Date_of_Admission']
            btype=request.form['bedtype']
            address=request.form['Address']
            state=request.form['State']
            city=request.form['City']
            db2=db.get_db()
            db2.execute('INSERT INTO patient(patient_id,patient_name,patient_age,date_of_admission,type_of_room,address,state,city,date_of_joining) VALUES (?,?,?,?,?,?,?,?,"9");',(pid,pname,page,doa,btype,address,state,city))
            return redirect('index')
        return render_template('addpatientdetails.html')
    @app.route('/view_patient',methods=('GET', 'POST'))
    def view_patient():
        db3=db.get_db()
        plist=db3.execute('SELECT * FROM patient').fetchall()
        return render_template('ViewPatient.html',plist=plist )
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('index'))
    
    db.init_app(app)

    return app

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
