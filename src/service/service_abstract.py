"""Doc."""

from abc import ABC, abstractmethod

from typing import List

from repository.repository import Repository

from model.auth.user import UserModel  # noqa: F401
from model.auth.role import RoleModel  # noqa: F401
from model.connection_type.connection_type import ConnectionTypeModel  # noqa: F401
from model.environment.environment import EnvironmentModel  # noqa: F401
from model.operating_system.operating_system import OperatingSystemModel  # noqa: F401
from model.server.server import ServerModel  # noqa: F401
from model.server.access import AccessModel  # noqa: F401
from model.server.service import ServiceModel  # noqa: F401


class ServiceAbstract(ABC):
    """Doc."""
    @property
    @abstractmethod
    def model(self):
        """Doc."""
        return self.model

    @model.setter
    @abstractmethod
    def model(self, model):
        self.model = model

    def get(
        id: int
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                ServiceAbstract.model
            ).get(
                ident=id
            )
        except Exception:
            raise
        else:
            return data
        finally:
            session.close()

    def get_all() -> List[object]:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                ServiceAbstract.model
            ).all()
        except Exception:
            raise
        else:
            return data
        finally:
            session.close()

    def get_by_filter(
        **kwargs
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                ServiceAbstract.model
            ).filter_by(
                **kwargs
            ).first()
        except Exception:
            raise
        else:
            return data
        finally:
            session.close()

    def get_by_filter_all(
        **kwargs
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                ServiceAbstract.model
            ).filter_by(
                **kwargs
            ).all()
        except Exception:
            raise
        else:
            return data
        finally:
            session.close()

    def add(
        obj_in: object
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            session.add(obj_in)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            session.refresh(obj_in)
            return obj_in
        finally:
            session.close()

    def edit(
        obj_in: object
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            session.add(obj_in)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            return obj_in
        finally:
            session.close()

    def delete(
        obj_in: object
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            session.delete(obj_in)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
            return obj_in
        finally:
            session.close()
