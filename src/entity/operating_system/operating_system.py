"""Doc."""


class OperatingSystem:
    """Doc."""
    def __init__(
        self,
        id: int = None,
        name: str = None,
        version: str = None,
        architect: str = None,
        is_active: bool = None
    ):
        """Constructor."""
        self.id = id
        self.name = name
        self.version = version
        self.architect = architect
        self.is_active = is_active
