"""Doc."""

from service.auth.role import role_service


def test_get_model():
    """Doc."""
    print()
    print("==========")
    print("Role: ", role_service.get_model())
    print("==========")


def xxx_test_get_role():
    """Doc."""
    role_id = 1
    role = role_service.get(id=role_id)
    print()
    print(role.role)
    print()
