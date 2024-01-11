from . import db

urls_ips = db.Table('urls_ips',
                    db.Column('url_id', db.BIGINT, db.ForeignKey('URLS.id'), primary_key=True),
                    db.Column('ip_id', db.INT, db.ForeignKey('IPS.id'), primary_key=True))


class URLS(db.Model):
    __tablename__ = 'URLS'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    ShortURL = db.Column(db.String(25))
    LongURL = db.Column(db.String(2500))
    Location = db.Column(db.String(40))
    user_id = db.Column(db.INT, db.ForeignKey('USERS.id'))
    Visits = db.Column(db.INT)
    ips = db.relationship('IPS', secondary=urls_ips, backref='URLS')


class USERS(db.Model):
    __tablename__ = 'USERS'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    PassWord = db.Column(db.String(25))
    API_SECRET_KEY =db.Column(db.String(128))


class IPS(db.Model):
    __tablename__ = 'IPS'

    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    address = db.Column(db.String(15))
