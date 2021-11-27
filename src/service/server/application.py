"""Doc."""

from service.service_abstract import ServiceAbstract

from model.server.application import ApplicationModel


class ApplicationService(ServiceAbstract):
    """Doc."""
    pass


application_service = ApplicationService(model=ApplicationModel)
