"""Doc."""

import jwt

from service.service_abstract import ServiceAbstract

from model.auth.user import UserModel

from werkzeug.security import check_password_hash


class UserService(ServiceAbstract):
    """Doc."""
    def authenticate(
        self,
        email: str,
        password: str
    ) -> UserModel:
        """Doc."""
        user = super().get_by_filter(email=email)

        if check_password_hash(pwhash=user.password, password=password):
            return user


user_service = UserService(model=UserModel)
