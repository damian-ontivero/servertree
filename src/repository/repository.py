"""Doc."""

from sqlalchemy.orm import Session

from model import db


class Repository:
    """Doc."""
    def get_session() -> Session:
        """Doc."""
        return db.session
