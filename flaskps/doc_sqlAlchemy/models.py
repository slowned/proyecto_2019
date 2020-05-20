from flaskps import db

# Ejemplo one-to-many
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)


# Ejemplo many-to-many
tags = db.Table('tags',
            db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
            db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
        )


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship(
            'Tag', secondary=tags, lazy='subquery',backref=db.backref('pages', lazy=True))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
