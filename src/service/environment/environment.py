"""Doc."""

from service.service_abstract import ServiceAbstract

from model.environment.environment import EnvironmentModel


class EnvironmentService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = EnvironmentModel
