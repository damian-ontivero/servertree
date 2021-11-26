"""Doc."""

from model import db


class ConnectionTypeModel(db.Base):
    """Connection Type table."""
    __tablename__ = "connection_type"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, is_active):
        """Constructor."""
        self.name = name
        self.is_active = is_active

    def __repr__(self):
        """Doc."""
        return "<ConnectionType: {}>".format(self.name)

    def save(self):
        """Doc."""
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        """Doc."""
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Doc."""
        return db.session.query(ConnectionTypeModel).all()

    @staticmethod
    def get_by_id(id):
        """Doc."""
        return db.session.query(ConnectionTypeModel).get(id)

    @staticmethod
    def get_by_name(name):
        """Doc."""
        return db.session.query(ConnectionTypeModel).filter_by(name=name).first()
