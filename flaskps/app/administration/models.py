from flaskps import db

from sqlalchemy_utils import ChoiceType

from .contants import SCHOOL_YEAR_CHOICES
from flaskps.utils.functions import get_today

__all__ = [
   'SchoolYear',
   'Workshop',
   'Lesson',
]


class Nucleos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    longitud = db.Column(db.Float)
    latitude = db.Column(db.Float)


class SchoolYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, default=get_today(), unique=True)
    end_date = db.Column(db.Date, default=get_today())
    semesters = db.Column(ChoiceType(SCHOOL_YEAR_CHOICES))
    workshops = db.relationship(
            'Workshop', backref='semester', lazy=True)
    active = db.Column(db.Boolean, default=True)

    @classmethod
    def create(cls, form):
        start_date = form.start_date.data
        end_date = form.end_date.data
        semesters = form.semester.data
        instance = cls(
                        start_date=start_date,
                        end_date=end_date,
                        semesters=semesters
                    )

        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return instance

    def add_workshop(self, workshops):
        for workshop in workshops:
            self.workshops.append(workshops)

    def delete(self):
        self.active = False
        db.session.commit()

    def update(self, form):
        self.start_date = form.start_date.data
        self.end_date = form.end_date.data
        self.semesters = form.semester.data
        db.session.commit()



workshop_students = db.Table('workshop_students',
    db.Column(
        'workshop_id', db.Integer, db.ForeignKey('workshop.id'), primary_key=True),
    db.Column(
        'student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
)


class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    short_name = db.Column(db.String(60))
    semester_id = db.Column(
        db.Integer, db.ForeignKey('school_year.id'), nullable=False)
    teacher_id = db.Column(
        db.Integer, db.ForeignKey('teachers.id'), nullable=True)
    students = db.relationship(
                    'Students',
                    secondary=workshop_students,
                    lazy='subquery',
                    backref=db.backref('workshops', lazy=True)
                )

    cant_lessons = db.Column(db.Integer, default=0)
    lessons = db.relationship('Lesson', backref='workshop', lazy=True)
    nucleo = db.Column(db.String(120))
    address = db.Column(db.String(214))
    days = db.Column(db.String(520))
    horario = db.Column(db.String(20))

    @classmethod
    def create(cls, form, sy):
        name = form.name.data
        short_name = form.short_name.data
        teacher_id = form.teacher.data
        nucleo = form.nucleo.data
        address = form.address.data
        days = form.days.data
        horario = form.horario.data
        cant = form.clases.data

        instance = cls(
            name=name,
            short_name=short_name,
            teacher_id=teacher_id,
            semester_id=sy.id,
            cant_lessons=cant,
            nucleo=nucleo,
            address=address,
            days=days,
            horario=horario,
        )

        n = 1
        for lesson in range(cant+1):
            l = Lesson(number=n, workshop_id=instance.id)
            n += 1
            instance.lessons.append(l)

        db.session.add(instance)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return instance

    def update(self, form):
        pass

    def add_student(self, student):
        self.students.append(student)
        for lesson in self.lessons:
            attend = Attend(lesson=lesson, student=student)
            db.session.add(attend)
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()


class Attend(db.Model):
    has_attended = db.Column(db.Boolean, default=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), primary_key=True)
    student = db.relationship('Students', backref='attend')
    lesson = db.relationship('Lesson', backref='attend')

    def attend(self):
        self.has_attended = True if not self.has_attended else False
        db.session.add(self)
        db.session.commit()


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
