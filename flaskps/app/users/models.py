from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from flaskps import db, login_manager
from flaskps.utils.models import TimeStampedModel


class User(db.Model, TimeStampedModel, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    active = db.Column(db.Boolean, default=True)
    password_hash = db.Column(db.String(128))
    # Define the relationship to Role via UserRoles
    roles = db.relationship('Rol', secondary='user_roles')

    def __repr__(self):
        return '<Usuario: %r>' % self.username

    @classmethod
    def create(cls, form):
        username = form.username.data
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        roles = form.roles.raw_data
        roles = Rol.query.filter(Rol.name.in_(roles)).all()

        instance = cls(
            name=name,
            surname=surname,
            username=username,
            email=email,
            password=password,
            roles=roles,
        )
        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return instance

    def update(self, form):
        self.name = form.name.data
        self.surname = form.surname.data
        self.username = form.username.data
        self.email = form.email.data
        self.active = form.active.data

        roles = form.roles.raw_data
        roles = Rol.query.filter(Rol.name.in_(roles)).all()
        self.roles = roles

        if not self.verify_password(form.password.data):
            self.password = form.password.data

        db.session.commit()

    @classmethod
    def delete(cls, user_id):
        user = User.query.filter_by(id=user_id).first_or_404()
        db.session.delete(user)
        db.session.commit()

    def have_permissions(self, permission):
        perm = []
        for rol in self.roles:
            perm += rol.permisos.split(',')
        if permission in perm:
            return True
        return False

    @property
    def is_active(self):
        return self.active

    @property
    def password(self):
        """
        Impide que se pueda leer la clave de usuario
        """
        raise AttributeError('password: no es un atributo de lectura. :D')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


## Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Rol(db.Model):
    """
    Create a Role table
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    permisos = db.Column(db.String(60000), nullable=False)

    def __init__(self, name, permisos):
        super().__init__
        self.name = name
        self.permisos = ','.join(permisos)

    def __repr__(self):
        return '<Rol: {}>'.format(self.name)


class UserRoles(db.Model):
        __tablename__ = 'user_roles'
        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
        role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
