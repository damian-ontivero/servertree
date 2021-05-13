from app import db

class Environment(db.Model):
    __tablename__ = 'Environments'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Environment {}>'.format(self.name)

    @staticmethod
    def get_all():
        return Environment.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Environment.query.get(id)

class OperatingSystem(db.Model):
    __tablename__ = 'OperatingSystems'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    architect = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return '{} - {} - {}'.format(self.name, self.version, self.architect)
    
    @staticmethod
    def get_all():
        return OperatingSystem.query.all()
    
    @staticmethod
    def get_by_id(id):
        return OperatingSystem.query.get(id)

class Server(db.Model):
    __tablename__ = 'Servers'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    environment_id = db.Column(db.Integer, db.ForeignKey('Environments.id'), nullable=False)
    operating_system_id = db.Column(db.Integer, db.ForeignKey('OperatingSystems.id'), nullable=False)
    cpu = db.Column(db.String(50), nullable=False)
    ram = db.Column(db.String(50), nullable=False)
    hdd = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, name, environment_id, operating_system_id, cpu, ram, hdd, is_active):
        self.name = name
        self.environment_id = environment_id
        self.operating_system_id = operating_system_id
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.is_active = is_active
    
    def __repr__(self):
        return f'<Server {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return Server.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Server.query.filter_by(name=name).first()
    
    @staticmethod
    def get_all():
        return Server.query.all()