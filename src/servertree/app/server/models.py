"""Doc."""

from servertree.app import db


class Server(db.Model):
    __tablename__ = 'Servers'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    environment_id = db.Column(db.Integer, db.ForeignKey('Environments.id'), nullable=False)
    operating_system_id = db.Column(db.Integer, db.ForeignKey('OperatingSystems.id'), nullable=False)
    cpu = db.Column(db.String(50), nullable=False)
    ram = db.Column(db.String(50), nullable=False)
    hdd = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, environment_id, operating_system_id, cpu, ram, hdd, is_active):
        self.name = name
        self.environment_id = environment_id
        self.operating_system_id = operating_system_id
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.is_active = is_active

    def __repr__(self):
        return f'<Server {self.name}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Server.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Server.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Server.query.all()


class Access(db.Model):
    __tablename__ = 'Access'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey('Servers.id'), nullable=False)
    connection_type_id = db.Column(db.Integer, db.ForeignKey('ConnectionType.id'), nullable=False)
    ip_local = db.Column(db.String(15))
    port_local = db.Column(db.String(5))
    ip_public = db.Column(db.String(15))
    port_public = db.Column(db.String(5))
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean)

    def __init__(self, server_id, connection_type_id, ip_local, port_local, ip_public, port_public, username, password, is_active):
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
        return '<Access_ID: {}>'.format(self.id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Access.query.all()

    @staticmethod
    def get_by_id(id):
        return Access.query.get(id)

    @staticmethod
    def get_by_server_id(server_id):
        return Access.query.filter_by(server_id=server_id).all()


class Service(db.Model):
    __tablename__ = 'Services'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey('Servers.id'), nullable=False)
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
        return '<Service_ID: {}>'.format(self.id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Service.query.all()

    @staticmethod
    def get_by_id(id):
        return Service.query.get(id)

    @staticmethod
    def get_by_server_id(server_id):
        return Service.query.filter_by(server_id=server_id).all()
