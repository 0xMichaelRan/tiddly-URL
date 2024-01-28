from itsdangerous import Serializer, SignatureExpired, BadSignature
import ReadConfig
from . import db
from passlib.apps import custom_app_context as pwd_context
config = ReadConfig.readconfig("./local_config.json")

urls_ips = db.Table('urls_ips',
                    db.Column('url_id', db.BIGINT, db.ForeignKey('URLS.id'), primary_key=True),
                    db.Column('ip_id', db.INT, db.ForeignKey('IPS.id'), primary_key=True))


class URLS(db.Model):
    __tablename__ = 'URLS'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    ShortURL = db.Column(db.String(25), index=True)
    LongURL = db.Column(db.String(2500))
    Location = db.Column(db.String(40))
    user_id = db.Column(db.INT, db.ForeignKey('USERS.id'))
    Visits = db.Column(db.INT,default=0)
    ips = db.relationship('IPS', secondary=urls_ips, backref='URLS')


class USERS(db.Model):
    __tablename__ = 'USERS'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)




class IPS(db.Model):
    __tablename__ = 'IPS'

    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    address = db.Column(db.String(15),index=True)
