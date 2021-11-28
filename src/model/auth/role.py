"""Doc."""

from model import db


class RoleModel(db.Base):
    """Role table."""
    __tablename__ = "role"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"
