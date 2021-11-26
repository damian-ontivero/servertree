"""Doc."""

from model import db


class RoleModel(db.Base):
    """Role table."""
    __tablename__ = "role"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        """Doc."""
        return "<Role {}>".format(self.role)

    @staticmethod
    def get_by_id(id):
        """Doc."""
        return db.session.query(RoleModel).get(id)

    @staticmethod
    def get_all():
        """Doc."""
        return db.session.query(RoleModel).all()
