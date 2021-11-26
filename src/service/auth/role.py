"""Doc."""

from service.service_abstract import ServiceAbstract

from model.auth.role import RoleModel


class RoleService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = RoleModel
