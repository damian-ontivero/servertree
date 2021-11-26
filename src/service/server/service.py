"""Doc."""

from service.service_abstract import ServiceAbstract

from model.server.service import ServiceModel


class ServiceService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = ServiceModel
