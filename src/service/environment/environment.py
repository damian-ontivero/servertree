"""Doc."""

from service.service_abstract import ServiceAbstract

from model.environment.environment import EnvironmentModel


class EnvironmentService(ServiceAbstract):
    """Doc."""
    pass


environment_service = EnvironmentService(model=EnvironmentModel)
