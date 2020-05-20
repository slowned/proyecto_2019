from flaskps import db
from sqlalchemy_utils import ChoiceType
from .constants import (
    GENDER_CHOICES,
)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(60))
    name = db.Column(db.String(60))
    birth_date = db.Column(db.Date())
    borned = db.Column(db.String(60))
    locality = db.Column(db.String(60))
    address = db.Column(db.String(60))
    gender = db.Column(ChoiceType(GENDER_CHOICES))
    document_type = db.Column(db.String(60))
    document_number = db.Column(db.String(60))
    tutor = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    tutor_name = db.Column(db.String(60))
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhood.id'), nullable=False)



    def __repr__(self):
        return '<Estudiante: %r>' % self.name

    @classmethod
    def create(cls, form):
        instance = cls(
            name=form.name.data,
            surname=form.surname.data,
            birth_date=form.birth_date.data,
            borned=form.borned.data,
            locality=form.locality.data,
            address=form.address.data,
            neighborhood_id=form.neighborhood.data,
            gender=form.gender.data,
            document_type=form.document_type.data,
            document_number=form.document_number.data,
            tutor=form.tutor.data,
            phone=form.phone.data,
            school_id=form.school.data,
            level_id=form.level.data,
            tutor_name=form.tutor_name.data,
        )
        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return instance

    @classmethod
    def delete(cls, student_id):
        student = Students.query.filter_by(id=student_id).first_or_404()
        db.session.delete(student)
        db.session.commit()

    def update(self, form):
        self.name = form.name.data
        self.surname = form.surname.data
        self.birth_date = form.birth_date.data
        self.borned = form.borned.data
        self.locality = form.locality.data
        self.address = form.address.data
        self.neighborhood = form.neighborhood.data
        self.gender = form.gender.data
        self.document_type = form.document_type.data
        self.document_number = form.document_number.data
        self.tutor = form.tutor.data
        self.phone = form.phone.data
        self.school = form.school.data
        self.level = form.level.data

        db.session.commit()


class Neighborhood(db.Model):
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(60), unique=True, nullable=False)

class Level(db.Model):
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(60), unique=True, nullable=False)

class School(db.Model):
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(60), unique=True, nullable=False)
        address = db.Column(db.String(100))
        phone = db.Column(db.String(20))
