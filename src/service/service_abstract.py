"""Doc."""

from typing import List

from repository.repository import Repository

from model.auth.user import UserModel  # noqa: F401
from model.auth.role import RoleModel  # noqa: F401
from model.connection_type.connection_type import ConnectionTypeModel  # noqa: F401
from model.environment.environment import EnvironmentModel  # noqa: F401
from model.operating_system.operating_system import OperatingSystemModel  # noqa: F401
from model.server.server import ServerModel  # noqa: F401
from model.server.access import AccessModel  # noqa: F401
from model.server.application import ApplicationModel  # noqa: F401


class ServiceAbstract:
    """Doc."""
    def __init__(self, model):
        """Constructor."""
        self.model = model

    def get_model(self):
        """Doc."""
        return self.model

    def get(
        self,
        id: int
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                self.model
            ).get(
                ident=id
            )
        except Exception:
            raise
        else:
            return data
        finally:
            session.close()

    def get_all(self) -> List[object]:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                self.model
            ).all()
        except Exception:
            raise
        else:
            return data
        finally:
            session.close()

    def get_by_filter(
        self,
        **kwargs
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                self.model
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
        self,
        **kwargs
    ) -> object:
        """Doc."""
        session = Repository.get_session()

        try:
            data = session.query(
                self.model
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
