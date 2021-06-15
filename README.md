# S E R V E R   T R E E

Made with Python (Flask), HTML, CSS3, JavaScript (A little) and SQLAlchemy as ORM.

## To run the application you will need:
#### Install the requeriments:
    pip install -r requirements.txt

#### Set the environment variable:
    export FLASK_APP=run -> Linux
    set FLASK_APP=run -> CMD
    $env:FLASK_APP = "run" -> PowerShell

#### DB:
The application is using sqlite as database and is placed in "app/servertree.db" but if you want to configure a different DBMS you might change the SQLALCHEMY_DATABASE_URI variable in the Config class.

##### To initialize the DB (just in case you don't use the included DB):
    flask db init -> Crea una estructura de directorios y ficheros necesarios para la ejecución de esta extensión. Se ejecuta solo una vez, al principio.

##### To create the DB or when you change the DB model:
    flask db migrate -> Navega entre los modelos en busca de actualizaciones y genera los ficheros de migración de base de datos con los cambios detectados.

    flask db upgrade -> Lleva a cabo la migración de la base de datos.    

##### Default data:
    Users roles:
    insert into Roles (name) values ('Administrador'), ('Observador')

    Admin user (pass = 123456):
    insert into Users (firstname, lastname, email, password, role_id, is_active) values ('Administrador', 'Administrador', 'admin@servertree.com', 'pbkdf2:sha256:150000$qghrCG8m$16a44c366d90f0eb0a97c2a4317089a27741a172d9a410d025ed6a7dd56f11a4', 1, 1)

    Environment:
    insert into Environments (name) values ('Desarrollo'), ('Prueba'), ('Preproducción'), ('Producción')

    Operating system:
    insert into OperatingSystems (name, version, architect) values ('Ubuntu', '20.04', '64-bit'), ('Windows Server', '2019', '64-bit')

    Connection type:
    insert into ConnectionType (name) values ('SSH'), ('RDP')

#### Run Flask:
    flask run

#### TODO
* ~~Fix favicon. Done~~
* ~~Add user logged to navbar and be able to edit my user. Done~~
* ~~Add module titles. Done~~
* ~~User role "observador" must be able to edit its own user. Done~~
* ~~User role "observador" must not be able to click on edit/delete buttons of access/service. Done~~
* ~~Edit user keeping same email (Should be possible). Done~~
* ~~Edit server using an existing name for an environment (Should not be possible). Done~~
* ~~Create module for environment. Done~~
* ~~Create module for operating system. Done~~
* ~~Create module for connection type. Done~~
