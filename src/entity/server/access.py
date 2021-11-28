"""Doc."""


class Access:
    """Doc."""
    def __init__(
        self,
        id: int = None,
        server_id: int = None,
        connection_type_id: int = None,
        ip_local: str = None,
        port_local: str = None,
        ip_public: str = None,
        port_public: str = None,
        username: str = None,
        password: str = None,
        is_active: bool = None
    ):
        """Constructor."""
        self.id = id
        self.server_id = server_id
        self.connection_type_id = connection_type_id
        self.ip_local = ip_local
        self.port_local = port_local
        self.ip_public = ip_public
        self.port_public = port_public
        self.username = username
        self.password = password
        self.is_active = is_active
