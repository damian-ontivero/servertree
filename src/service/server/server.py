"""Doc."""

from service.service_abstract import ServiceAbstract

from model.server.server import ServerModel


class ServerService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = ServerModel
