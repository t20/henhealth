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
    appointment = db_session.query(Appointment). \
                        filter_by(patient_id=patient_id). \
                        filter_by(provider_id=provider_id). \
                        order_by(Appointment.appointment_date.desc()).first()
    return appointment

def get_medication(patient_id):
    """docstring for get_medication"""
    medications = db_session.query(Medication). \
                        filter_by(patient_id=patient_id). \
                        all()
    return medications

def get_discharge_checklists(patient_id):
    """docstring for get_discharge_form"""
    pdcs = db_session.query(PatientDischargeChecklist). \
                        filter_by(patient_id=patient_id). \
                        all()
    return pdcs

def get_providers_with_access(patient_id):
    #TODO - Chnage model name
    providers = db_session.query(Viewer). \
                filter_by(patient_id=patient_id). \
                filter_by(provider_id != None). \
                all()
    return providers

def get_caregivers_with_access(patient_id):
    #TODO - Chnage model name
    caregivers = db_session.query(Viewer). \
                filter_by(patient_id=patient_id). \
                filter_by(caregiver_id != None).all()
    return caregivers

def give_access(patient_id, caregiver_id=None, provider_id=None, commit=False):
    v = Viewer(patient_id, caregiver_id=caregiver_id, provider_id=provider_id)
    db_session.add(v)
    if commit:
        db_session.commit()

def get_discharge_checklist(discharge_checklist_id):
    """docstring for get_discharge_checklist"""
    dc = db_session.query(DischargeChecklist). \
                filter_by(id=discharge_checklist_id). \
                first()
    return dc

def add_question(patient_id, question_id, question_asked, question_notes, commit=False):
    discharge_response = DischargeResponse(patient_id, question_id, question_asked, question_notes)
    db_session.add(discharge_response)
    if commit:
        db_session.commit()

if __name__ == '__main__':
    app.debug = True
    app.run()
