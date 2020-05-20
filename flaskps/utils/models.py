from flaskps import db

from flaskps.utils.functions import get_today

class TimeStampedModel():
    created_at = db.Column(db.Date, default=get_today())
    updated_at = db.Column(db.Date, onupdate=get_today())
