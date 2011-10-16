from flask import Flask
app = Flask(__name__)

from database import db_session
from flask import render_template, request, session, redirect, url_for, flash
from models import *


@app.route('/')
def index():
    return "Index Page!"

@app.route('/hello')
def hello_world():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User page"

@app.route('/')
def login():
    """docstring for login"""
    pass


@app.route('/')
def regsiter():
    """docstring for regsiter"""
    pass


@app.route('/test')
def testbydt():
    """test ..."""
    pass


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
