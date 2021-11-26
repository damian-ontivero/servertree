"""Doc."""

from model import db

from model.auth.user import UserModel

from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    """Doc."""
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