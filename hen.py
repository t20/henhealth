from flask import Flask, request, render_template, redirect

app = Flask(__name__)

from database import db_session
from flask import render_template, request, session, redirect, url_for, flash
from models import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    """docstring for login"""
    return render_template('login.html')


@app.route('/register')
def regsiter():
    """docstring for regsiter"""
    return render_template('register.html')


@app.route('/forgot')
def forgot():
    """docstring"""
    return render_template('forgot.html')


@app.route('/account')
def account():
    """docstring"""
    return render_template('account.html')

def get_appointments(patient_id, provider_id):
    appointments = db_session.query(Appointment). \
                        filter_by(patient_id=patient_id). \
                        filter_by(provider_id=provider_id). \
                        order_by(Appointment.appointment_date.desc()).all()
    return appointments

def get_medication(patient_id):
    """docstring for get_medication"""
    medications = db_session.query(Medication). \
                        filter_by(patient_id=patient_id). \
    return medications

def get_discharge_checklists(patient_id):
    """docstring for get_discharge_form"""
    discharge_checklists = db_session.query(DischargeForm). \
                        filter_by(patient_id=patient_id). \
    return discharge_checklists

def get_users(user_id):
    


if __name__ == '__main__':
    app.debug = True
    app.run()
