"""Doc."""

from service.auth.user import UserService


def xxx_test_get_user():
    """Doc."""
    user_id = 1
    user = UserService.get(id=user_id)
    for attr in vars(user):
        print(attr)


def test_get_user_by_filter():
    """Doc."""
    email = "admin@servertree.com"
    user = UserService.get_by_filter(email=email)
    print(user.email)