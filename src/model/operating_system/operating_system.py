"""Doc."""

from model import db


class OperatingSystemModel(db.Base):
    """Operating System table."""
    __tablename__ = "operating_system"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    architect = db.Column(db.String(6), nullable=False)
    is_active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f"{self.name} {self.version} {self.architect}"
