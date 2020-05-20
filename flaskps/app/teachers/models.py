from flaskps import db


class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(60))
    name = db.Column(db.String(60))
    birth_date = db.Column(db.Date())
    locality = db.Column(db.String(60))
    address = db.Column(db.String(60))
    document_type = db.Column(db.String(60))
    document_number = db.Column(db.String(60))
    phone = db.Column(db.String(60))

    def __repr__(self):
        return '<Docente: %r>' % self.name

    @classmethod
    def delete(cls, teacher_id):
        teacher = Teachers.query.filter_by(id=teacher_id).first_or_404()
        db.session.delete(teacher)
        db.session.commit()

    @classmethod
    def create(cls, form):
        teacher = Teachers(
            name=form.name.data,
            surname=form.surname.data,
            birth_date=form.birth_date.data,
            locality=form.locality.data,
            address=form.address.data,
            document_type=form.document_type.data,
            document_number=form.document_number.data,
            phone=form.phone.data,
        )
        db.session.add(teacher)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return teacher

    def update(self, form):
        self.name = form.name.data
        self.surname = form.surname.data
        self.birth_date = form.birth_date.data
        self.locality = form.locality.data
        self.address = form.address.data
        self.document_type = form.document_type.data
        self.document_number = form.document_number.data
        self.phone = form.phone.data

        db.session.commit()
