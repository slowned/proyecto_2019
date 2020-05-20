import os
import datetime
from flaskps import db, BASE_DIR

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(60))
    inventory_number = db.Column(db.String(60))
    img_path = db.Column(db.String(120))
    cant = 0

    def __repr__(self):
        return '<Instrumento: %r>' % self.name

    @classmethod
    def set_inventory_number(cls,type):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        cls.cant+=1
        c = cls.cant
        return type+str(year)+str(month)+str(c)

    @classmethod
    def create(cls, form, path):
        name = form.name.data
        type = form.type.data
        inventory_number = cls.set_inventory_number(type)
        img_path = path
        instance = cls(name=name,type=type,inventory_number=inventory_number,img_path=img_path)

        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return instance

    @classmethod
    def delete(cls, instrument_id):
        instrument = cls.query.filter_by(id=instrument_id).first_or_404()
        os.remove('%s/flaskps' % BASE_DIR+instrument.img_path)
        db.session.delete(instrument)
        db.session.commit()

    def update(self, form, path):
        self.name = form.name.data
        self.type = form.type.data
        self.img_path = path
        db.session.commit()
