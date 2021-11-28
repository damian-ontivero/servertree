"""Doc."""

from typing import List

from repository.repository import Repository


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
        self,
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
        self,
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
        self,
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
