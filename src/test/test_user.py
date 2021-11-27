"""Doc."""

from service.auth.user import user_service


def test_get_model():
    """Doc."""
    print()
    print("==========")
    print("User: ", user_service.get_model())
    print("==========")


def xxx_test_get_user():
    """Doc."""
    user_id = 1
    user = user_service.get(id=user_id)
    print()
    print(user.email)
    print(user.password)
    print()


def xxx_test_get_user_by_filter():
    """Doc."""
    user_id = 1
    user = user_service.get_by_filter(id=user_id)
    print("==========")
    print(user.email)
    print(user.password)
    print("==========")
