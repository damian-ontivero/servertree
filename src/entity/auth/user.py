"""Doc."""


class User:
    """Doc."""
    def __init__(
        self,
        id: int = None,
        firstname: str = None,
        lastname: str = None,
        email: str = None,
        password: str = None,
        role_id: int = None,
        is_active: bool = None
    ):
        """Constructor."""
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role_id = role_id
        self.is_active = is_active
