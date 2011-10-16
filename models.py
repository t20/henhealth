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
    """docstring for Patient"""
    def __init__(self, arg):
        super(Patient, self).__init__()
        self.arg = arg
	
	__tablename__ = 'patient'
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

class Provider(object):
		
	__tablename__ = 'patient'
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
    """docstring for Caregiver"""
    def __init__(self, arg):
        super(Caregiver, self).__init__()
        self.arg = arg

	__tablename__ = 'caregiver'
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
    """docstring for Medicine"""
    def __init__(self, arg):
        super(Medicine, self).__init__()
        self.arg = arg

	__tablename__ = 'medicine'
	id = Column(Integer, primary_key=True)
	medicine_name = Column(String(50), nullable=False)
	usage = Column(String(50), nullable=False)
	side_effects = Column(String(50), nullable=False)
	comments = Column(String(150), nullable=False)

class Appointments(object):
	
	__tablename__ = 'appointments'
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patient.id'))
	provider_id = Column(Integer, ForeignKey('provider.id'))
	date = Column(DateTime)
	time = Column(DateTime)
	address = Column(String(50), nullable=False)
	
class DischargeForm(object):
	
	__tablename__ = 'discharge_form'
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patient.id'))
	provider_id = Column(Integer, ForeignKey('provider.id'))

class Medication(object):
	
	__tablename__ = 'medication'
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patient.id'))
	medicine_id = Column(Integer, ForeignKey('patient.id'))
	
class Viewer(object):
	
	__tablename__ = 'medication'
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey('patient.id'))
	provider_id = Column(Integer, ForeignKey('provider.id'))
	caregiver_id = Column(Integer, ForeignKey('caregiver.id'))