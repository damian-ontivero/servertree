"""Doc."""

from model import db


class ConnectionTypeModel(db.Base):
    """Connection Type table."""
    __tablename__ = "connection_type"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)
