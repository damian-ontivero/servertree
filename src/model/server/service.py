"""Doc."""

from model import db


class ServiceModel(db.Base):
    """Service table."""
    __tablename__ = "service"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey("server.id"), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    architect = db.Column(db.String(6), nullable=False)
    ip_local = db.Column(db.String(15))
    port_local = db.Column(db.String(5))
    ip_public = db.Column(db.String(15))
    port_public = db.Column(db.String(5))
    install_dir = db.Column(db.String(50), nullable=False)
    log_dir = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    server = db.relationship("ServerModel", foreign_keys=[server_id])
