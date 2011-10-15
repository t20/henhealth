class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
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

class Patient(object):
    """docstring for Patient"""
    def __init__(self, arg):
        super(Patient, self).__init__()
        self.arg = arg


class Medicine(object):
    """docstring for Medicine"""
    def __init__(self, arg):
        super(Medicine, self).__init__()
        self.arg = arg
        