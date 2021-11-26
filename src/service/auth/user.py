"""Doc."""

from typing import List

from sqlalchemy.orm import joinedload

from repository.repository import Repository

from model.auth.user import UserModel


class UserService:
    """Doc."""
    @staticmethod
    def get_by_id(
        id: int
    ) -> UserModel:
        """Doc."""
        session = Repository.get_session()

        try:
            user = session.query(
                UserModel
            ).get(id)
        except Exception:
            raise
        else:
            return user
        finally:
            session.close()

    @staticmethod
    def get_by_email(
        email: str
    ) -> UserModel:
        """Doc."""
        session = Repository.get_session()

        try:
            user = session.query(
                UserModel
            ).filter_by(
                email=email
            ).first()
        except Exception:
            raise
        else:
            return user
        finally:
            session.close()

    @staticmethod
    def get_all() -> List[UserModel]:
        """Doc."""
        session = Repository.get_session()

        try:
            user_list = session.query(
                UserModel
            ).options(
                joinedload("role")
            ).all()
        except Exception:
            raise
        else:
            return user_list
        finally:
            session.close()

    @staticmethod
    def add(
        user: UserModel
    ) -> UserModel:
        """Doc."""
        session = Repository.get_session()

        try:
            session.add(user)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            session.refresh(user)
            return user
        finally:
            session.close()

    @staticmethod
    def edit(
        user: UserModel
    ) -> UserModel:
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

    @staticmethod
    def delete(
        user: UserModel
    ) -> UserModel:
        """Doc."""
        session = Repository.get_session()

        try:
            session.delete(user)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            return user
        finally:
            session.close()
