from app import db

class Environment(db.Model):
    __tablename__ = 'Environments'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Environment {}>'.format(self.name)

    @staticmethod
    def get_all():
        return Environment.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Environment.query.get(id)