### CREDENCIALES ACCESO
administrador
usuario: admin@admin.com
pass: admin

docente
usuario: usudocente@mail.com
pass: 123456

preceptor
usuario: usupreceptor@mail.com
pass:123456
# Remember that a model is a representation of a database table in code.

# crear base de datos
```console
mysql -u root
create user 'admin'@'localhost' identified by 'admin';
create database grupo8;
grant all privileges on grupo8 .* to 'admin'@'localhost';
```

### crear tablas con sqlalchemy
 Utilizamos sqlalchemy como ORB (Object-relational mapping) para facilitar el modelado y la manipulacion de datos.

```console
sh runshell.sh
>>> from flaskps import db
>>> db.create_all()
```

### output de ejemplo Model User y Rol
> 2019-11-14 22:00:37,395 INFO sqlalchemy.engine.base.Engine COMMIT
> 2019-11-14 22:00:37,398 INFO sqlalchemy.engine.base.Engine
> CREATE TABLE users (
> 	created_at DATE,
> 	updated_at DATE,
> 	id INTEGER NOT NULL AUTO_INCREMENT,
> 	is_admin BOOL,
> 	username VARCHAR(60) NOT NULL,
> 	email VARCHAR(60) NOT NULL,
> 	name VARCHAR(60),
> 	surname VARCHAR(60),
> 	active BOOL,
> 	password_hash VARCHAR(128),
> 	PRIMARY KEY (id),
> 	CHECK (is_admin IN (0, 1)),
> 	UNIQUE (username),
> 	UNIQUE (email),
> 	CHECK (active IN (0, 1))
> )
>
>
> 2019-11-14 22:00:37,398 INFO sqlalchemy.engine.base.Engine {}
> 2019-11-14 22:00:37,432 INFO sqlalchemy.engine.base.Engine COMMIT
> 2019-11-14 22:00:37,433 INFO sqlalchemy.engine.base.Engine
> CREATE TABLE rol (
> 	id INTEGER NOT NULL AUTO_INCREMENT,
> 	name VARCHAR(60) NOT NULL,
> 	PRIMARY KEY (id),
> 	UNIQUE (name)
> )






## Correr servidor local localhost:5000
```console
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```


### Estructura (Blueprints)

Home - tendra las declaradas las vistas de home y dashboard
Admin - tendra todo lo relacionado con la administracion (dependiendo del roll) forms and views
Auth - tendra todo lo relacionado con la autenticacion (login, exepciones) forms and views

> └── dream-team
>     ├── flaskps
>     │   ├── __init__.py
>     │   ├── admin
>     │   │   ├── __init__.py
>     │   │   ├── forms.py
>     │   │   └── views.py
>     │   ├── auth
>     │   │   ├── __init__.py
>     │   │   ├── forms.py
>     │   │   └── views.py
>     │   ├── home
>     │   │   ├── __init__.py
>     │   │   └── views.py
>     │   ├── models.py
>     │   ├── static
>     │   └── templates
>     ├── config.py
>     ├── instance
>     │   └── config.py
>     ├── migrations
>     │   ├── README
>     │   ├── alembic.ini
>     │   ├── env.py
>     │   ├── script.py.mako
>     │   └── versions
>     │       └── a1a1d8b30202_.py
>     ├── requirements.txt
>     └── run.py


### instanciar base de datos y crear Objetos inicial para el correcto funcionamiento


* entrar a la consola de flask

```console
sh flask_shell.sh
```

**set de datos bases**

```python
from flaskps import db
db.create_all()

from flaskps.app.users.models import User, Rol
from flaskps.app.users.constants import *
from flaskps.app.configurations.models import Configurations
from flaskps.app.students.constants import BARRIOS, ESCUELAS
from flaskps.app.students.models import School, Neighborhood, Level
from flaskps.app.administration.models import Nucleos

# crea usuario
user = User(
    username='superadmin',
    email='admin@admin.com',
)
user.password = 'admin'

# lo guarda en la db

conf = Configurations(
  description='escuela orquesta beriso',
  title='escuela orquesta',
  email='escuela@orquesta.mail.com'
)
db.session.add(conf)

docente = Rol(name='docente', permisos=DOCENTE_PERMISOS)
administrador = Rol(name='administrador', permisos=ADMIN_PERMISOS)
preceptor = Rol(name='preceptor', permisos=PRECEPTOR_PERMISOS)

db.session.add(docente)
db.session.add(administrador)
db.session.add(preceptor)

user.roles.append(administrador)
db.session.add(user)


for n in range(1,12):
  nivel = Level(name=n)
  db.session.add(nivel)

for n in BARRIOS:
  barrio= Neighborhood(name=n)
  db.session.add(barrio)

for n in ESCUELAS:
  escuela = School(name=n, address='Calle 123', phone='123123')
  db.session.add(escuela)

n1 = Nucleos(name='Nucleo Berisso', longitud=-34.922763, latitude=-57.9860357)
n2 = Nucleos(name='Nucleo Centro', longitud=-34.897606, latitude=-57.9653306)
n3 = Nucleos(name='Nucleo Numero 1', longitud=-34.911029, latitude=-57.9547927)
n4 = Nucleos(name='Nucleo Numero 2', longitud=-34.931573, latitude=-57.9341207)

db.session.add(n1)
db.session.add(n2)
db.session.add(n3)
db.session.add(n4)

db.session.commit()
```
