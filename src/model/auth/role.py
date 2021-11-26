"""Doc."""

from model import db


class RoleModel(db.Base):
    """Role table."""
    __tablename__ = "role"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role = db.Column(db.String(30), unique=True, nullable=False)
