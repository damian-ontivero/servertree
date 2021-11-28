"""Doc."""

from model import db

from flask_login import UserMixin


class UserModel(db.Base, UserMixin):
    """User table."""
    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    is_active = db.Column(db.Boolean)

    role = db.relationship("RoleModel", foreign_keys=[role_id], lazy="joined")

    def __repr__(self) -> str:
        return f"{self.name}"
