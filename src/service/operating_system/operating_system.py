"""Doc."""

from service.service_abstract import ServiceAbstract

from model.operating_system.operating_system import OperatingSystemModel


class OperatingSystemService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = OperatingSystemModel
