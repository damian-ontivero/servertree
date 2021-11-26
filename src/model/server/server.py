"""Doc."""

from model import db


class ServerModel(db.Base):
    """Server table."""
    __tablename__ = "server"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    environment_id = db.Column(db.Integer, db.ForeignKey("environment.id"), nullable=False)
    operating_system_id = db.Column(db.Integer, db.ForeignKey("operating_system.id"), nullable=False)
    cpu = db.Column(db.String(50), nullable=False)
    ram = db.Column(db.String(50), nullable=False)
    hdd = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    environment = db.relationship("EnvironmentModel", foreign_keys=[environment_id])

    operating_system = db.relationship("OperatingSystemModel", foreign_keys=[operating_system_id])

    def __init__(self, name, environment_id, operating_system_id, cpu, ram, hdd, is_active):
        """Constructor."""
        self.name = name
        self.environment_id = environment_id
        self.operating_system_id = operating_system_id
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.is_active = is_active

    def __repr__(self):
        """Doc."""
        return f"<Server {self.name}>"

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
    def get_by_id(id):
        """Doc."""
        return db.session.query(ServerModel).get(id)

    @staticmethod
    def get_by_name(name):
        """Doc."""
        return db.session.query(ServerModel).filter_by(name=name).first()

    @staticmethod
    def get_all():
        """Doc."""
        return db.session.query(ServerModel).all()
