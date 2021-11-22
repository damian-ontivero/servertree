"""Doc."""

from app.servertree import db


class ConnectionType(db.Model):
    __tablename__ = "ConnectionType"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, is_active):
        self.name = name
        self.is_active = is_active

    def __repr__(self):
        return "<ConnectionType: {}>".format(self.name)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ConnectionType.query.all()

    @staticmethod
    def get_by_id(id):
        return ConnectionType.query.get(id)

    @staticmethod
    def get_by_name(name):
        return ConnectionType.query.filter_by(name=name).first()
