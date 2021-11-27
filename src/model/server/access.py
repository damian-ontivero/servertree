"""Doc."""

from model import db


class AccessModel(db.Base):
    """Access table."""
    __tablename__ = "access"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey("server.id"), nullable=False)
    connection_type_id = db.Column(db.Integer, db.ForeignKey("connection_type.id"), nullable=False)
    ip_local = db.Column(db.String(15))
    port_local = db.Column(db.String(5))
    ip_public = db.Column(db.String(15))
    port_public = db.Column(db.String(5))
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    server = db.relationship("ServerModel", foreign_keys=[server_id], lazy="joined")
    connection_type = db.relationship("ConnectionTypeModel", foreign_keys=[connection_type_id], lazy="joined")
