"""Doc."""

from service.service_abstract import ServiceAbstract

from model.auth.user import UserModel


class UserService(ServiceAbstract):
    """Doc."""
    ServiceAbstract.model = UserModel
