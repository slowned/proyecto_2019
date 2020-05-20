# TODO LIST

# Ciclo lectivo (shool_year)
  * en el template del edit cuando se guarda el mismo semestre guarda el VALUE y deveria quedarse con el nombre
  


# creacion de roles con sus permisos

```console
from flaskps import db
from flaskps.app.users.models import Rol, User
from flaskps.app.users.constants import *
from flaskps.app.configurations.models import Configurations

user = User(
    username='superadmin',
    email='admin@admin.com',
)
user.password = 'admin'
db.session.add(user)

conf = Configurations(
  description='escuela orquesta beriso',
  title='escuela orquesta',
  email='escuela@orquesta.mail.com'
)
db.session.add(conf)

administrador = Rol('administrador', ADMIN_PERMISOS)
docente = Rol('docente', DOCENTE_PERMISOS)
preceptor = Rol('preceptor', PRECEPTOR_PERMISOS)

db.session.add(administrador)
db.session.add(docente)
db.session.add(preceptor)

user.roles.append(administrador)

db.session.commit()
```
>>>>>>> 42609108a9e38cbb309480b4a106c1564d4e1467
