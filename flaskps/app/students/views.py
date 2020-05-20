import requests
from sqlalchemy import and_
from flask_login import login_required
from flask import render_template, redirect, request, url_for, flash
from flask_user import current_user

from flaskps import db
from . import students
from .models import Students, Level, School, Neighborhood
from .forms import CreateStudentsForm
from flaskps.app.configurations.models import Configurations


@students.route('/students/create', methods=['GET', 'POST'])
@login_required
def create(permiso='students_new'):
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateStudentsForm(request.form)
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()
        levels = Level.query.filter_by()
        neighborhoods = Neighborhood.query.filter_by()
        schools = School.query.filter_by()
        if request.method == 'POST':
            if form.validate():
                student = Students.query.filter(
                    and_(
                        Students.document_number == form.document_number.data,
                        Students.document_type == form.document_type.data,
                    )
                ).all()

                if student:
                    msg = "Error al crear usuario: ya existe un usuario con el mismo documento y tipo"
                    return render_template(
                        'students/create.html',
                        form=form,
                        dniTypes=dniTypes,
                        localities=localities,
                        msg=msg,
                    ), 403
                student = Students.create(form)
                return redirect(url_for('students.detail', student_id=student.id))
        return render_template('students/create.html', form=form, dniTypes=dniTypes, localities=localities, levels=levels, neighborhoods=neighborhoods, schools=schools)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@students.route('/students/list/', methods=['GET'], defaults={'page': 1})
@students.route('/students/list/<int:page>', methods=['GET'])
@login_required
def list(page, permiso='students_index'):
    if current_user.have_permissions(permiso):
        page = page
        conf = Configurations.query.first()
        students = Students.query.filter_by()
        students = students.paginate(page, conf.offset_paginator, False)
        return render_template('students/list.html', students=students)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@students.route('/students/detail/<int:student_id>', methods=['GET', 'POST'])
@login_required
def detail(student_id, permiso='students_show'):
    if current_user.have_permissions(permiso):
        student = Students.query.filter_by(id=student_id).first_or_404()
        level = Level.query.filter_by(id=student.level_id).first_or_404()
        neighborhood = Neighborhood.query.filter_by(id=student.neighborhood_id).first_or_404()
        school = School.query.filter_by(id=student.school_id).first_or_404()
        return render_template('students/detail.html', student=student, level=level, neighborhood=neighborhood, school=school)
    else:
        return render_template('home/dashboard.html')

@students.route('/students/delete/<int:student_id>', methods=['POST'])
@login_required
def delete(student_id, permiso='students_destroy'):
    if current_user.have_permissions(permiso):
        Students.delete(student_id)
        return redirect('/students/list')
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@students.route('/students/update/<int:student_id>', methods=['GET', 'POST'])
@login_required
def update(student_id, permiso='students_update'):
    if current_user.have_permissions(permiso):
        student = Students.query.filter_by(id=student_id).first_or_404()
        dniTypes = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento").json()
        localities = requests.get("https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad").json()
        form = CreateStudentsForm(request.form)
        levels = Level.query.filter_by()
        neighborhoods = Neighborhood.query.filter_by()
        schools = School.query.filter_by()
        if request.method == "POST":
            if form.validate():
                student.update(form)
                return redirect(url_for('students.detail', student_id=student.id))
        return render_template('students/edit.html', student=student, localities=localities, dniTypes=dniTypes, form=form, levels=levels, neighborhoods=neighborhoods, schools=schools), 200
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')
