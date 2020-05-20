from sqlalchemy import and_
import requests
from flask_login import login_required
from flask_user import current_user

from flask import render_template, redirect, request, url_for, flash

from flaskps import db
from . import teachers
from .models import Teachers
from .forms import CreateTeachersForm
from flaskps.app.configurations.models import Configurations


@teachers.route('/teachers/create', methods=['GET', 'POST'])
@login_required
def create(permiso='teachers_new'):
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateTeachersForm(request.form)
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()

        if request.method == 'POST':
            if form.validate():
                teacher = Teachers.query.filter(
                    and_(
                        Teachers.document_number == form.document_number.data,
                        Teachers.document_type == form.document_type.data,
                    )
                ).all()

                if teacher:
                    msg = "error: ya existe un maestro con ese tipo y numero de docuemtno"
                    return render_template(
                        'teachers/create.html',
                        form=form,
                        dniTypes=dniTypes,
                        localities=localities,
                        msg=msg,
                    ), 403

                teacher = Teachers.create(form)
                msg = "El Docente %s se creo con exito" % teacher.name
                return redirect(
                        url_for('teachers.detail', teacher_id=teacher.id))
        return render_template('teachers/create.html', form=form, dniTypes=dniTypes, localities=localities)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@teachers.route('/teachers/list/', methods=['GET'], defaults={'page': 1})
@teachers.route('/teachers/list/<int:page>', methods=['GET'])
@login_required
def list(page, permiso='teachers_index'):
    if current_user.have_permissions(permiso):
        page = page
        conf = Configurations.query.first()
        teachers = Teachers.query.filter_by()
        teachers = teachers.paginate(page, conf.offset_paginator, False)
        return render_template('teachers/list.html', teachers=teachers)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@teachers.route('/teachers/detail/<int:teacher_id>', methods=['GET', 'POST'])
@login_required
def detail(teacher_id, permiso='teachers_show'):
    if current_user.have_permissions(permiso):
        teacher = Teachers.query.filter_by(id=teacher_id).first_or_404()
        return render_template('teachers/detail.html', teacher=teacher)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@teachers.route('/teachers/delete/<int:teacher_id>', methods=['POST'])
@login_required
def delete(teacher_id, permiso='teachers_destroy'):
    if current_user.have_permissions(permiso):
        Teachers.delete(teacher_id)
        return redirect(url_for('teachers.list'))
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@teachers.route('/teachers/update/<int:teacher_id>', methods=['GET', 'POST'])
@login_required
def update(teacher_id,permiso='teachers_update'):
    if current_user.have_permissions(permiso):
        teacher = Teachers.query.filter_by(id=teacher_id).first_or_404()
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()
        form = CreateTeachersForm(request.form)
        if request.method == "POST":
            if form.validate():
                teacher.update(form)
                return redirect(url_for('teachers.detail', teacher_id=teacher.id))
        return render_template('teachers/edit.html', teacher=teacher, dniTypes=dniTypes, localities=localities, form=form), 200
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')
