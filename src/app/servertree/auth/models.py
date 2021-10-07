"""Doc."""

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from app.servertree import db


class Role(db.Model):
    __tablename__ = 'Roles'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Role {}>'.format(self.role)

    @staticmethod
    def get_by_id(id):
        return Role.query.get(id)

    @staticmethod
    def get_all():
        return Role.query.all()


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, firstname, lastname, email, role_id, is_active):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.role_id = role_id
        self.is_active = is_active

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return User.query.all()
