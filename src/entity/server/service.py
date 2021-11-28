"""Doc."""


class Service:
    """Doc."""
    def __init__(
        self,
        id: int = None,
        server_id: int = None,
        service: str = None,
        version: str = None,
        architect: str = None,
        ip_local: str = None,
        port_local: str = None,
        ip_public: str = None,
        port_public: str = None,
        install_dir: str = None,
        log_dir: str = None,
        is_active: bool = None
    ):
        """Constructor."""
        self.id = id
        self.server_id = server_id
        self.service = service
        self.version = version
        self.architect = architect
        self.ip_local = ip_local
        self.port_local = port_local
        self.ip_public = ip_public
        self.port_public = port_public
        self.install_dir = install_dir
        self.log_dir = log_dir
        self.is_active = is_active
