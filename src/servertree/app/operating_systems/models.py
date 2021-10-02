from servertree.app import db


class OperatingSystem(db.Model):
    __tablename__ = 'OperatingSystems'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    architect = db.Column(db.String(6), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, version, architect, is_active):
        self.name = name
        self.version = version
        self.architect = architect
        self.is_active = is_active

    def __repr__(self):
        return '{} - {} - {}'.format(self.name, self.version, self.architect)
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return OperatingSystem.query.all()
    
    @staticmethod
    def get_by_id(id):
        return OperatingSystem.query.get(id)
    
    @staticmethod
    def get_by_name_version_architect(name, version, architect):
        return OperatingSystem.query.filter_by(name=name, version=version, architect=architect).first()
