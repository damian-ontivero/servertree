"""Doc."""

from model import db


class ServiceModel(db.Base):
    """Service table."""
    __tablename__ = "service"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey("server.id"), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    architect = db.Column(db.String(6), nullable=False)
    ip_local = db.Column(db.String(15))
    port_local = db.Column(db.String(5))
    ip_public = db.Column(db.String(15))
    port_public = db.Column(db.String(5))
    install_dir = db.Column(db.String(50), nullable=False)
    log_dir = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    server = db.relationship("ServerModel", foreign_keys=[server_id])

    def __init__(
        self,
        server_id,
        service,
        version,
        architect,
        ip_local,
        port_local,
        ip_public,
        port_public,
        install_dir,
        log_dir,
        is_active
    ):
        """Constructor."""
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

    def __repr__(self):
        """Doc."""
        return "<Service {}>".format(self.id)

    def save(self):
        """Doc."""
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        """Doc."""
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Doc."""
        return db.session.query(ServiceModel).all()

    @staticmethod
    def get_by_id(id):
        """Doc."""
        return db.session.query(ServiceModel).get(id)

    @staticmethod
    def get_by_server_id(server_id):
        """Doc."""
        return db.session.query(ServiceModel).filter_by(server_id=server_id).all()
