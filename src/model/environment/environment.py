"""Doc."""

from model import db


class EnvironmentModel(db.Base):
    """Environment table."""
    __tablename__ = "environment"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f"{self.name}"
