"""Doc."""

from service.service_abstract import ServiceAbstract

from model.server.access import AccessModel


class AccessService(ServiceAbstract):
    """Doc."""
    pass


access_service = AccessService(model=AccessModel)
