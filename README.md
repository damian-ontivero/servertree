# S E R V E R   T R E E

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

## TODO
* Add user logged to navbar.
* Add module title.
* Fix user role "observador" to be able to edit its own user.
* Fix user role "observador" to not be able to edit/delete access/service.
* Fix edit user keeping same email (Should be possible).
* Fix edit server using an existing name (Should not be possible).
* Create module for environment.
* Create module for operating system.