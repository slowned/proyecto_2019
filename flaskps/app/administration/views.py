import datetime
import json
from sqlalchemy import and_
from flaskps import db
from flask_login import login_required
from flask import render_template, redirect, request, url_for, flash
from flask_user import current_user

from . import administration
from .models import SchoolYear, Workshop, Attend, Nucleos
from .forms import CreateSchoolYearForm, WorkshopCreateForm
from .contants import TALLERES
from flaskps.app.configurations.models import Configurations
from flaskps.app.teachers.models import Teachers
from flaskps.app.students.models import Students, Neighborhood


@administration.route('/school-year/create', methods=['GET', 'POST'])
@login_required
def school_year_create(permiso='administration_new'):
    """
    metodo GET: renderiza form de creacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateSchoolYearForm(request.form)
        if request.method == 'POST':
            if form.validate():
                school_year = SchoolYear.query.filter_by(start_date=form.start_date.data).all()
                if school_year:
                    msg = "Error al crear el ciclo lectivo ya existe uno creado con la misma fecha de inicio"
                    return render_template(
                        'administration/school_year_create.html',
                        form=form,
                        msg=msg
                    )

                school_year = SchoolYear.create(form)
                return redirect(url_for('administration.school_year_detail', school_year_id=school_year.id))
        return render_template('administration/school_year_create.html', form=form)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/school-year/delete/<int:school_year_id>', methods=['POST'])
@login_required
def school_year_delete(school_year_id, permiso='administration_destroy'):
    if current_user.have_permissions(permiso):
        sy = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
        sy.delete()
        return redirect('/school-year/list')
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')

@administration.route('/school-year/edit/<int:school_year_id>', methods=['GET', 'POST'])
@login_required
def school_year_edit(school_year_id, permiso='administration_new'):
    if current_user.have_permissions(permiso):
        form = CreateSchoolYearForm(request.form)
        school_year_edit = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
        if request.method == "POST":
            if form.validate():
                school_year = SchoolYear.query.filter_by(start_date=form.start_date.data).all()
                if school_year:
                    if not school_year_id == school_year[0].id:
                        msg = "Error al editar, ya existe un ciclo lectivo con la misma fecha de inicio."
                        return render_template(
                            'administration/school_year_edit.html',
                            form=form,
                            msg=msg,
                            school_year=school_year_edit
                        )
                school_year_edit.update(form)
                return redirect(url_for('administration.school_year_detail', school_year_id=school_year_edit.id))
        return render_template('administration/school_year_edit.html', school_year=school_year_edit)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/school-year/detail/<int:school_year_id>', methods=['GET'])
@login_required
def school_year_detail(school_year_id, permiso='administration_show'):
    if current_user.have_permissions(permiso):
        school_year = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
        teachers = Teachers.query.all()
        return render_template(
            'administration/school_year_detail.html', school_year=school_year, teachers=teachers)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/school-year/list', methods=['GET'], defaults={'page':1})
@administration.route('/school-year/list/<int:page>', methods=['GET'])
@login_required
def school_year_list(page, permiso='administration_index'):
    if current_user.have_permissions(permiso):
        conf = Configurations.query.first()
        school_years = SchoolYear.query.filter_by(active=True).paginate(
                            page,
                            conf.offset_paginator,
                            False
                        )

        return render_template(
                'administration/school_year_list.html', school_years=school_years)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/workshop/craete/<int:school_year_id>', methods=['GET', 'POST'])
@login_required
def workshop_create(school_year_id, permiso='administration_new'):
    if current_user.have_permissions(permiso):
        sy = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
        teachers = Teachers.query.all()
        nucleos = Neighborhood.query.all()
        form = WorkshopCreateForm(request.form)
        if request.method == "POST" and form.validate():
            workshop = Workshop.create(form, sy)
            return redirect(
                    url_for('administration.workshop_detail', workshop_id=workshop.id, school_year_id=school_year_id))
        return render_template(
                    'administration/workshop_create.html',
                    school_year=sy,
                    nucleos= nucleos,
                    teachers=teachers,
                    form=form,
                    talleres=TALLERES,
                )
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/workshop/detail/<int:workshop_id>/<int:school_year_id>', methods=['GET'])
@login_required
def workshop_detail(workshop_id, school_year_id,permiso='administration_show'):
    if current_user.have_permissions(permiso):
        school_year = SchoolYear.query.filter_by(id=school_year_id).first_or_404()
        workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
        teacher = Teachers.query.filter_by(id=workshop.teacher_id).first_or_404()
        return render_template(
                'administration/workshop_detail.html',
                workshop=workshop,
                teacher=teacher,
                school_year=school_year
        )
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')

@administration.route('/administration/map', methods=['GET'])
@login_required
def show_map():
    nucleos = Nucleos.query.filter_by().all()
    return render_template('administration/map.html', nucleos=nucleos)


@administration.route('/workshop/list', methods=['GET'])
@login_required
def workshop_list():
    pass


# @administration.route('/workshop/add-lesson/<int:workshop_id>', methods=['POST'])
# # @login_required
# def workshop_add_leson(workshop_id):
#     workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
#     form = LessonCreateForm(request.form)
#     if request.method == "POST" and form.validate():
#         lesson = Lesson.create()
#         workshop.add_lesson()
#     return render_template('administration/workshop_detail.html', workshop=workshop)



@administration.route('/workshop/students-list/<int:workshop_id>', methods=['GET'])
@login_required
def show_workshop_students(workshop_id, permiso='students_index'):
    if current_user.have_permissions(permiso):
        workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
        return render_template(
                'administration/workshop_show_students.html',
                workshop=workshop,
            )
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/workshop/add_student/<int:workshop_id>', methods=['GET', 'POST'])
@login_required
def add_student(workshop_id, permiso='students_index'):
    if current_user.have_permissions(permiso):
        workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
        students = Students.query.all()
        return render_template(
                'administration/workshop_add_student.html',
                workshop=workshop,
                students=students,
            )
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@administration.route('/workshop/lesson_attend/', methods=['POST'])
@login_required
def attend(permiso='students_index'):  # TODO: ver permiso
    if current_user.have_permissions(permiso):
        student_id = request.json.get('student_id')
        lesson_id = request.json.get('lesson_id')

        attend = Attend.query.filter(
            and_(
                Attend.lesson_id == lesson_id,
                Attend.student_id == student_id
            )
        ).first_or_404()
        attend.attend()
        workshop = Workshop.query.filter_by(id=attend.lesson.workshop_id).first_or_404()
        return render_template(
                'administration/workshop_show_students.html',
                workshop=workshop,
            )
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')

@administration.route('/workshop/workshop_add_student/<int:workshop_id>/<int:student_id>', methods=['GET'])
@login_required
def workshop_add_student(workshop_id, student_id, permiso='students_index'):
    if current_user.have_permissions(permiso):
        workshop = Workshop.query.filter_by(id=workshop_id).first_or_404()
        student = Students.query.filter_by(id=student_id).first_or_404()
        if can_add_student(student, workshop):
            workshop.add_student(student)
            msg = "el alumno {} se agrego al taller".format(student.name)
        else:
            msg = "el alumno {} no se agrego al taller".format(student.name)
        return redirect(
            url_for('administration.add_student', workshop_id=workshop.id, msg=msg))
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


def can_add_student(student, workshop):
    if student in workshop.students:
        return False
    else:
        return True
