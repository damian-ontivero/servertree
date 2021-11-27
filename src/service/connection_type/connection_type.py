"""Doc."""

from service.service_abstract import ServiceAbstract

from model.connection_type.connection_type import ConnectionTypeModel


class ConnectionTypeService(ServiceAbstract):
    """Doc."""
    pass


connection_type_service = ConnectionTypeService(model=ConnectionTypeModel)
