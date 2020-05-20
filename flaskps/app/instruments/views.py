from sqlalchemy import or_
import requests, os
from flask_login import login_required
from flask_user import current_user

from flask import render_template, redirect, request, url_for, flash

from flaskps import db, BASE_DIR
from .models import Instrument
from .forms import CreateInstrumentsForm
from . import instruments
from flaskps.app.configurations.models import Configurations
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
MAX_IMAGE_SIZE = 0.5 * 1024 * 1024
UPLOAD_IMAGES_FOLDER = '%s/flaskps/static/uploads/' % BASE_DIR,
IMG_PATH = '/static/uploads/'

@instruments.route('/instruments/create', methods=['GET', 'POST'])
@login_required
def create(permiso='administration_new'):
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateInstrumentsForm(request.form)
        if request.method == 'POST' and form.validate():
            if request.files:
                image = request.files["image"]
                if image.filename == '':
                    return redirect(request.url)
                if not allowed_file(image.filename):
                    return redirect(request.url)
                else:
                    image_name = secure_filename(image.filename)
                    image.save(os.path.join(UPLOAD_IMAGES_FOLDER[0], image_name))
                img_path= IMG_PATH+image_name

            instrument = Instrument.create(form,img_path)
            return redirect(url_for('instruments.detail',instrument_id=instrument.id))
        return render_template('instruments/create.html', form=form)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@instruments.route('/instruments/detail/<int:instrument_id>', methods=['GET','POST'])
@login_required
def detail(instrument_id,permiso='administration_show'):
    if current_user.have_permissions(permiso):
        instrument = Instrument.query.filter_by(id=instrument_id).first_or_404()
        return render_template('instruments/detail.html', instrument=instrument)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@instruments.route('/instruments/list/', methods=['GET', 'POST'], defaults={'page':1})
@instruments.route('/instruments/list/<int:page>', methods=['GET'])
@login_required
def list(page,permiso='administration_index'):
    if current_user.have_permissions(permiso):
        page = page
        conf = Configurations.query.first()
        instruments = Instrument.query.filter_by()
        msg_query = None
        if request.method == 'POST':
            form = dict(request.form)
            instrument_name = form.get('instrument_name')
            inventory_number = form.get('inventory_number')
            if instrument_name or inventory_number:
                instruments = Instrument.query.filter(
                    or_(
                        Instrument.name == instrument_name,
                        Instrument.inventory_number == inventory_number
                    )
                )
            if not instruments.all():
                msg_query = "No se encontraron resultados"
        instruments = instruments.paginate(page, conf.offset_paginator, False)
        return render_template(
            'instruments/list.html',
            instruments=instruments,
            msg_query=msg_query
        )
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@instruments.route('/instruments/update/<int:instrument_id>', methods=['GET', 'POST'])
@login_required
def update(instrument_id,permiso='administration_update'):
    if current_user.have_permissions(permiso):
        instrument = Instrument.query.filter_by(id=instrument_id).first_or_404()
        form = CreateInstrumentsForm(request.form)
        if request.method == "POST":
            if request.files["image"].filename:
                image = request.files["image"]
                if image.filename == '':
                    return redirect(request.url)
                if not allowed_file(image.filename):
                    return redirect(request.url)
                else:
                    image_name = secure_filename(image.filename)
                    image.save(os.path.join(UPLOAD_IMAGES_FOLDER[0], image_name))
                    try:
                        os.remove('%s/flaskps' % BASE_DIR+instrument.img_path)
                    except Exception as e:
                        pass
                img_path = IMG_PATH+image_name
            else:
                img_path = instrument.img_path
            if form.validate():
                instrument.update(form, img_path)
                return redirect(url_for('instruments.detail', instrument_id=instrument.id))
        return render_template('instruments/edit.html', instrument=instrument, form=form), 200
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')


@instruments.route('/instruments/delete/<int:instrument_id>', methods=['POST'])
@login_required
def delete(instrument_id, permiso='administration_destroy'):
    if current_user.have_permissions(permiso):
        Instrument.delete(instrument_id)
        return redirect(url_for('instruments.list'))
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')
