"""Doc."""

from service.service_abstract import ServiceAbstract

from model.auth.role import RoleModel


class RoleService(ServiceAbstract):
    """Doc."""
    pass


role_service = RoleService(model=RoleModel)
