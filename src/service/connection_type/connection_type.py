"""Doc."""

from service.service_abstract import ServiceAbstract

from model.connection_type.connection_type import ConnectionTypeModel


class ConnectionTypeService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = ConnectionTypeModel
