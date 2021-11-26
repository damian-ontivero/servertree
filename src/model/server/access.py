"""Doc."""

from model import db


class AccessModel(db.Base):
    """Access table."""
    __tablename__ = "access"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey("server.id"), nullable=False)
    connection_type_id = db.Column(db.Integer, db.ForeignKey("connection_type.id"), nullable=False)
    ip_local = db.Column(db.String(15))
    port_local = db.Column(db.String(5))
    ip_public = db.Column(db.String(15))
    port_public = db.Column(db.String(5))
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    server = db.relationship("ServerModel", foreign_keys=[server_id])

    connection_type = db.relationship("ConnectionTypeModel", foreign_keys=[connection_type_id])

    def __init__(self, server_id, connection_type_id, ip_local, port_local, ip_public, port_public, username, password, is_active):
        """Constructor."""
        self.server_id = server_id
        self.connection_type_id = connection_type_id
        self.ip_local = ip_local
        self.port_local = port_local
        self.ip_public = ip_public
        self.port_public = port_public
        self.username = username
        self.password = password
        self.is_active = is_active

    def __repr__(self):
        """Doc."""
        return "<Access {}>".format(self.id)

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
        return db.session.query(AccessModel).all()

    @staticmethod
    def get_by_id(id):
        """Doc."""
        return db.session.query(AccessModel).get(id)

    @staticmethod
    def get_by_server_id(server_id):
        """Doc."""
        return db.session.query(AccessModel).filter_by(server_id=server_id).all()
