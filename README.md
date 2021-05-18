# S E R V E R   T R E E

## To run the application you will need:
#### Install the requeriments:
    pip install -r requirements.txt

#### Set the environment variable:
    export FLASK_APP=run -> Linux
    set FLASK_APP=run -> CMD
    $env:FLASK_APP = "run" -> PowerShell
    
#### Run Flask:
    flask run
    
#### Default data:
    Users roles:
    insert into Roles values (1, 'Administrador'), (2, 'Observador')

    Admin user:
    insert into Users values (1, 'Administrador', 'Administrador', 'admin@servertree.com', 'pbkdf2:sha256:150000$qghrCG8m$16a44c366d90f0eb0a97c2a4317089a27741a172d9a410d025ed6a7dd56f11a4', 1, 1)

    Environment:
    insert into Environments values (1, 'Desarrollo'), (2, 'Prueba'), (3, 'Preproducción'), (4, 'Producción')

    Operating system:
    insert into OperatingSystems values (1, 'Ubuntu', '20.04', '64-bit'), (2, 'Windows Server', '2019', '64-bit')

    Connection type:
    insert into ConnectionType values (1, 'SSH'), (2, 'RDP')

## Notes:
The application is using sqlite as database and is include in "app/servertree.db" but if you want to configure a different DBMS you might change the SQLALCHEMY_DATABASE_URI variable in the Config class.

#### To initialize the DB (just once at the first):
    flask db init -> Crea una estructura de directorios y ficheros necesarios para la ejecución de esta extensión. Se ejecuta solo una vez, al principio.

#### In case that you change the DB model:
    flask db migrate -> Navega entre los modelos en busca de actualizaciones y genera los ficheros de migración de base de datos con los cambios detectados.

    flask db upgrade -> Lleva a cabo la migración de la base de datos.
