"""Doc."""

from model import db

from model.auth.role import RoleModel


class RoleService:
    """Doc."""
    @staticmethod
    def get_by_id(id):
        """Doc."""
        return db.session.query(RoleModel).get(id)

    @staticmethod
    def get_all():
        """Doc."""
        return db.session.query(RoleModel).all()