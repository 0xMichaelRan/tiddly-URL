from . import db


class URLS(db.Model):
    __tablename__ = 'URLS'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    ShortURL = db.Column(db.String(10))
    LongURL = db.Column(db.String(100))
