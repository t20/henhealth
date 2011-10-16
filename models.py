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

""""

class Patient(object):
	__tablename__ = 'patients'

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
    password = Column(String(225), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created = Column(DateTime)
    modified = Column(DateTime)

class Provider(object):
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
	
class Caregiver(object):
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

class Medicine(object):
    __tablename__ = 'medicine'
    
	id = Column(Integer, primary_key=True)
	medicine_name = Column(String(50), nullable=False)
	usage = Column(String(50), nullable=False)
	side_effects = Column(Text, nullable=False)
	comments = Column(Text, nullable=False)

class Appointments(object):
	__tablename__ = 'appointments'
    
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patients.id'))
	provider_id = Column(Integer, ForeignKey('providers.id'))
	appointment_date = Column(DateTime)
	appointment_time = Column(DateTime)
	address = Column(String(200), nullable=False)

class PatientDischargeChecklist(object):
	__tablename__ = 'patient_discharge_checklists'
    
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patients.id'))
	discharge_checklist = Column(Integer, ForeignKey('discharge_checklists.id'))

class DischargeChecklist(object):
    __tablename__ = 'discharge_checklists'
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patients.id'))
	provider_id = Column(Integer, ForeignKey('providers.id'))
	date = Column(DateTime)
	
	# What's Ahead
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
	
	

class Medication(object):
	__tablename__ = 'medications'
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patients.id'))
	medicine_id = Column(Integer, ForeignKey('patients.id'))

class Viewer(object):
	__tablename__ = 'viewers'
    
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patients.id'))
	provider_id = Column(Integer, ForeignKey('providers.id'))
	caregiver_id = Column(Integer, ForeignKey('caregivers.id'))
