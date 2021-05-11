# S E R V E R   T R E E

## To run the application you will need:
#### Install the requeriments:
    pip install -r requirements.txt

#### Set the environment variable:
    FLASK_APP=run

#### Run Flask:
    flask run
    
#### Web access include:
    User: admin@servertree.com
    Password 123456

## Notes:
The application is using sqlite as database and is include in "app/servertree.db" but if you want to configure a different DBMS you might change the SQLALCHEMY_DATABASE_URI variable in the Config class.

#### To initialize the DB (just once at the first):
    flask db init -> Crea una estructura de directorios y ficheros necesarios para la ejecución de esta extensión. Se ejecuta solo una vez, al principio.

#### In case that you change the DB model:
    flask db migrate -> Navega entre los modelos en busca de actualizaciones y genera los ficheros de migración de base de datos con los cambios detectados.

    flask db upgrade -> Lleva a cabo la migración de la base de datos.
