"""Doc."""


class Server:
    """Doc."""
    def __init__(
        self,
        id: int = None,
        name: str = None,
        environment_id: int = None,
        operating_system_id: int = None,
        cpu: str = None,
        ram: str = None,
        hdd: str = None,
        is_active: bool = None
    ):
        """Constructor."""
        self.id = id
        self.name = name
        self.environment_id = environment_id
        self.operating_system_id = operating_system_id
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.is_active = is_active
