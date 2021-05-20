from app import db

class ConnectionType(db.Model):
    __tablename__ = 'ConnectionType'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<ConnectionType: {}>'.format(self.name)

    @staticmethod
    def get_all():
        return ConnectionType.query.all()
    
    @staticmethod
    def get_by_id(id):
        return ConnectionType.query.get(id)