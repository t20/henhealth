from flask import Flask, request, render_template, redirect

app = Flask(__name__)

from database import db_session
from flask import render_template, request, session, redirect, url_for, flash
from functools import wraps
from models import *

app.config.from_object('config')
app.secret_key = app.config['APP_SECRET_KEY']

######DECORATORS
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#######ROUTING METHODS

@app.route('/login', methods=['GET', 'POST'])
def login():
    """docstring for login"""
    if request.method == 'POST':
        username = request.form['username']
        if username == 'patient':
            session['user_id'] = 1
            return redirect(url_for('dashboard'))
        if username == 'provider':
            session['user_id'] = 2
            return redirect(url_for('provider_dashboard'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/forgot')
def forgot():
    """docstring"""
    return render_template('forgot.html')


@app.route('/account')
def account():
    """docstring"""
    return render_template('account.html')


@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session.get('user_id')
    provider_id = 2
    return render_template('patient_dashboard.html', 
                medications=get_medication(user_id),
                pdcs = get_discharge_checklists(user_id),
                appointment=get_appointments(user_id, provider_id),
                providers=get_providers_with_access(user_id),
                caregivers=get_caregivers_with_access(user_id)
                )

@app.route('/provider/dashboard')
def provider_dashboard():
    return render_template('provider_dashboard.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdc_checklist')
def pdc_checklist():
    """docstring for pdc_checklist"""
    return render_template('pdc_checklist.html')

@app.route('/register')
def regsiter():
    """docstring for regsiter"""
    return render_template('register.html')


@app.route('/forgot')
def forgot():
    """docstring"""
    return render_template('forgot.html')


@app.route('/account')
@login_required
def account():
    """docstring"""
    return render_template('account.html')


@app.route('/patient_dashboard')
@login_required
def patient_dashboard():
    """docstring"""
    return render_template('patient_dashboard.html')


@app.route('/checklist/<checklist_id>')
@login_required
def checklist_show():
    checklist = db_session.query(DischargeChecklist). \
                filter_by(id=checklist_id).first()
    return render_template('checklist_show.html', checklist=checklist, edit=False)


@app.route('/checklist/edit/<checklist_id>')
@login_required
def checklist_edit():
    checklist = db_session.query(DischargeChecklist). \
                filter_by(id=checklist_id).first()
    return render_template('checklist_form.html', checklist=checklist, edit=True)


@app.route('/checklist/new')
@login_required
def checklist_new():
    checklist = DischargeChecklist()
    user_id = session.get('user_id')
    return render_template('checklist_form', checklist=checklist, user_id=user_id)

####HELPER METHODS

def get_appointments(patient_id, provider_id):
    appointment = db_session.query(Appointment). \
                        filter_by(patient_id=patient_id). \
                        filter_by(provider_id=provider_id). \
                        order_by(Appointment.appointment_date.desc()).first()
    return appointment

def get_medication(patient_id):
    """docstring for get_medication"""
    medications = db_session.query(Medication).join(DischargeChecklist). \
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
    providers = db_session.query(Viewer). \
                filter_by(patient_id=patient_id). \
                filter(Viewer.provider_id != None). \
                all()
    return providers

def get_caregivers_with_access(patient_id):
    caregivers = db_session.query(Viewer). \
                filter_by(patient_id=patient_id). \
                filter(Viewer.caregiver_id != None). \
                all()
    return caregivers

def give_access(patient_id, caregiver_id=None, provider_id=None, commit=False):
    v = Viewer(patient_id, caregiver_id=caregiver_id, provider_id=provider_id)
    db_session.add(v)
    if commit:
        db_session.commit()

def revoke_access():
    access = db_session.query(Viewer). \
        filter_by(patient_id=patient_id, provider_id=provider_id). \
        all()
    session.delete(access)

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
    discharge_checklists = db_session.query(DischargeForm). \
                        filter_by(patient_id=patient_id).all()
    return discharge_checklists

if __name__ == '__main__':
    app.debug = True
    app.run()
