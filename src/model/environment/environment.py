"""Doc."""

from model import db


class EnvironmentModel(db.Base):
    """Environment table."""
    __tablename__ = "environment"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, is_active):
        """Constructor."""
        self.name = name
        self.is_active = is_active

    def __repr__(self):
        """Doc."""
        return "<Environment {}>".format(self.name)

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
        return EnvironmentModel.query.all()

    @staticmethod
    def get_by_id(id):
        """Doc."""
        return EnvironmentModel.query.get(id)

    @staticmethod
    def get_by_name(name):
        """Doc."""
        return EnvironmentModel.query.filter_by(name=name).first()
