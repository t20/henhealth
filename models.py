from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, backref
from database import Base
from datetime import datetime

"""class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(boolean, nullable=False)
    birthday = Column(DateTime)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip = Column(String(9), nullable=False)
    phone_number = Column(String(10), nullable=False)
    password = Column(String(150), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created = Column(DateTime)
    modified = Column(DateTime)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.created = datetime.now()
        self.modified = self.created

    def __repr__(self):
        return '<User %r>' % (self.name)

"""

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Boolean, nullable=False)
    birthday = Column(DateTime)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip = Column(String(9), nullable=False)
    phone_number = Column(String(10), nullable=False)
    password = Column(String(225), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created = Column(DateTime)
    modified = Column(DateTime)

class Provider(Base):
    __tablename__ = 'providers'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip = Column(String(9), nullable=False)
    phone_number = Column(String(10), nullable=False)
    password = Column(String(150), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created = Column(DateTime)
    modified = Column(DateTime)
    
class Caregiver(Base):
    __tablename__ = 'caregivers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip = Column(String(9), nullable=False)
    phone_number = Column(String(10), nullable=False)
    password = Column(String(150), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created = Column(DateTime)
    modified = Column(DateTime)

class Medicine(Base):
    __tablename__ = 'medicine'
    
    id = Column(Integer, primary_key=True)
    medicine_name = Column(String(50), nullable=False)
    usage = Column(String(50), nullable=False)
    side_effects = Column(Text, nullable=False)
    comments = Column(Text)
    
    def __init__(self, medicine_name=None, usage=None, side_effects=None, comments=None):
        self.medicine_name = medicine_name
        self.usage = usage
        self.side_effects = side_effects
        self.comments = comments
        
class Appointments(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    provider_id = Column(Integer, ForeignKey('providers.id'))
    appointment_date = Column(DateTime)
    appointment_time = Column(DateTime)
    address = Column(String(200))

    def __init__(self, patient_id=None, provider_id=None, appointment_date=None, appointment_time=None, address=None):
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.address = address

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)

class PatientDischargeChecklist(Base):
    __tablename__ = 'patient_discharge_checklists'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    discharge_checklist = Column(Integer, ForeignKey('discharge_checklists.id'))

class DischargeChecklist(Base):
    __tablename__ = 'discharge_checklists'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    provider_id = Column(Integer, ForeignKey('providers.id'))
    date = Column(DateTime)

class DischargeChecklistResponse(Base):
    __tablename__ = 'discharge_checklists_response'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question_asked = Column(Boolean, nullable=False)
    question_notes = Column(Text)
    
    def __init__(self, question_id=None, question_asked=None, question_notes=None):
        self.question_id = question_id
        self.question_asked = question_asked
        self.question_notes = question_notes

class DischargeChecklistResponseMapping(Base):
    __tablename__ = 'discharge_checklists_response_mapping'
    id = Column(Integer, primary_key=True)
    discharge_checklist = Column(Integer, ForeignKey('discharge_checklists.id'))
    discharge_checklist_response_id = Column(Integer, ForeignKey('discharge_checklists_response.id'))

"""    # What's Ahead
    care_after_discharge = Column(String(255), nullable=False)
    caregiver_id = Column(Integer, ForeignKey('caregivers.id')) #family care
    
    # Your Condition
    health_condition = Column(String(255), nullable=False)
    improvement_options = Column(String(255), nullable=False)
    problems_to_watch_out_for = Column(String(255), nullable=True)
    medication_id = Column(Integer, ForeignKey('medications.id'))
    
    # Recovery and Support
    medical_equipment_needs = Column(String(255), nullable=True)
    activity_help_needed = Column(String(255), nullable=True)
    task_help_needed = Column(String(255), nullable=True)
    social_group_info = Column(String(255), nullable=True)
    insurance_info_needs = Column(String(255), nullable=True)
    written_discharge_instructions = Column(String(255), nullable=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    
    # Caregiver
    caregiver_questions = Column(String(255), nullable=True)
    provider_concerns = Column(String(255), nullable=True)
    special_instructions = Column(String(255), nullable=True)
"""

class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    medicine_id = Column(Integer, ForeignKey('patients.id'))

class Viewer(Base):
    __tablename__ = 'viewers'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    provider_id = Column(Integer, ForeignKey('providers.id'))
    caregiver_id = Column(Integer, ForeignKey('caregivers.id'))
