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

    environment = db.relationship("EnvironmentModel", foreign_keys=[environment_id], lazy="joined")
    operating_system = db.relationship("OperatingSystemModel", foreign_keys=[operating_system_id], lazy="joined")
