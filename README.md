# S E R V E R   T R E E

Made with Python (Flask), HTML, CSS3, JavaScript (A little) and SQLAlchemy as ORM.

## To run the application you will need:
#### Install the requeriments:
    pip install -r requirements.txt

#### Set the environment variable:
    export FLASK_APP=entrypoint -> Linux
    set FLASK_APP=entrypoint -> CMD
    $env:FLASK_APP = "entrypoint" -> PowerShell

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

#### Run Flask:
    flask run

#### Some screenshots:
![image](https://user-images.githubusercontent.com/62670542/122008826-be488680-cdb9-11eb-88f5-a57efbe095b4.png)
![image](https://user-images.githubusercontent.com/62670542/122009078-049de580-cdba-11eb-9b74-4006b9bb6061.png)
![image](https://user-images.githubusercontent.com/62670542/122009098-08316c80-cdba-11eb-917b-7c99a64bbe08.png)
![image](https://user-images.githubusercontent.com/62670542/122009122-0ebfe400-cdba-11eb-9f44-6607b08a66d6.png)
![image](https://user-images.githubusercontent.com/62670542/122009138-12536b00-cdba-11eb-96f6-83754c57fbaf.png)
![image](https://user-images.githubusercontent.com/62670542/122009157-167f8880-cdba-11eb-90f9-e429671da507.png)
![image](https://user-images.githubusercontent.com/62670542/122009165-197a7900-cdba-11eb-8ba1-93e531145805.png)
![image](https://user-images.githubusercontent.com/62670542/122009214-24350e00-cdba-11eb-8b6a-677129793c45.png)


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
