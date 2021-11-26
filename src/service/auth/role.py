"""Doc."""

from typing import List

from repository.repository import Repository

from model.auth.role import RoleModel


class RoleService:
    """Doc."""
    @staticmethod
    def get_by_id(
        id: int
    ) -> RoleModel:
        """Doc."""
        session = Repository.get_session()
        return session.query(RoleModel).get(id)

    @staticmethod
    def get_all() -> List[RoleModel]:
        """Doc."""
        session = Repository.get_session()
        return session.query(RoleModel).all()

    @staticmethod
    def add(
        user: RoleModel
    ) -> RoleModel:
        """Doc."""
        session = Repository.get_session()

        try:
            session.add(user)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            return user
        finally:
            session.close()
