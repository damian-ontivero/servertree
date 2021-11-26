"""Doc."""

from model import db


class OperatingSystemModel(db.Base):
    """Operating System table."""
    __tablename__ = "operating_system"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    architect = db.Column(db.String(6), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, version, architect, is_active):
        """Constructor."""
        self.name = name
        self.version = version
        self.architect = architect
        self.is_active = is_active

    def __repr__(self):
        """Doc."""
        return "{0} - {1} - {2}".format(self.name, self.version, self.architect)

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
        return db.session.query(OperatingSystemModel).all()

    @staticmethod
    def get_by_id(id):
        """Doc."""
        return db.session.query(OperatingSystemModel).get(id)

    @staticmethod
    def get_by_name_version_architect(name, version, architect):
        """Doc."""
        return db.session.query(OperatingSystemModel).filter_by(name=name, version=version, architect=architect).first()
