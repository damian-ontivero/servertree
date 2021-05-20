from app import db

class OperatingSystem(db.Model):
    __tablename__ = 'OperatingSystems'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
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