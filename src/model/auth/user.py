"""Doc."""

from model import db

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


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

    role = db.relationship("RoleModel", foreign_keys=[role_id])

    def __init__(self, firstname, lastname, email, role_id, is_active):
        """Constructor."""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.role_id = role_id
        self.is_active = is_active

    def __repr__(self):
        """Doc."""
        return f"<User {self.email}>"

    def set_password(self, password):
        """Doc."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Doc."""
        return check_password_hash(self.password, password)

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
        return db.session.query(UserModel).get(id)

    @staticmethod
    def get_by_email(email):
        """Doc."""
        return db.session.query(UserModel).filter_by(email=email).first()

    @staticmethod
    def get_all():
        """Doc."""
        return db.session.query(UserModel).all()
