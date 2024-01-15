from datetime import timedelta

from flask import request, jsonify, abort, redirect, render_template, session, url_for, flash, g
from .. import db
from . import main
from .. import models
from .. import Change
from flask_jwt_extended import create_access_token

from ..decorators import login_required, visit_count

config = models.config
BASE_URL = config['BASEURL']


@main.route('/', methods=['GET'])
@login_required
def index():
    ip = request.remote_addr
    return render_template("index.html")


@main.route('/login/', methods=['GET', 'POST'])
def login():
    session['login'] = False
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        pwdInData = models.USERS.query.filter_by(username=username).first()
        if pwdInData == None:  # 用户不存在
            flash('用户不存在')
        else:
            if pwdInData.verify_password(password):  # 登录成功
                session['login'] = True
                session['username'] = username
                session['user_id'] = pwdInData.id
                return redirect(url_for("main.index"))
            else:
                flash('密码错误')
    return render_template('login.html')


@main.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        pwdInData = models.USERS.query.filter_by(username=username).first()
        if pwdInData != None:  # 用户已存在
            flash('用户已存在')
        else:
            user = models.USERS(username=username)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            flash('注册成功请进行登录')
            return redirect(url_for("main.login"))

    return render_template('register.html')


@main.route('/logout/')
@login_required
def admin_logout():
    session['login'] = False
    session['username'] = None
    flash('Log out successfully!')
    return redirect(url_for('main.login'))


@main.route('/shorten/', methods=['POST'])
@login_required
def shorten():
    long_url = request.form['long_url']
    user_id = session['user_id']
    jsondata = {}

    url = models.URLS.query.filter_by(LongURL=long_url, user_id=user_id).first()
    if url is not None:
        jsondata['long'] = url.LongURL
        jsondata['short'] = url.ShortURL
        jsondata['location'] = url.Location

    else:
        url = models.URLS(LongURL=long_url, user_id=user_id)
        db.session.add(url)
        db.session.commit()

        # url = models.URLS.query.filter_by(LongURL=long_url).first()
        a = Change.ShortURL()
        short_url = a.encode(url.id)

        url.ShortURL = short_url
        url.Location = BASE_URL + short_url
        jsondata['long'] = url.LongURL
        jsondata['short'] = url.ShortURL
        jsondata['location'] = url.Location

        db.session.commit()

    return jsonify(jsondata)


@main.route('/lengthen/', methods=['POST'])
def lengthen():
    location = request.form['location'].strip()
    url = models.URLS.query.filter_by(Location=location).first()
    jsondata = {}

    if url is not None:
        a = Change.ShortURL()
        id = a.decode(url.ShortURL)
        url = models.URLS.query.get(id)
        jsondata['long'] = url.LongURL
    else:
        jsondata['status'] = 'False'
    return jsonify(jsondata)


@main.route('/<short>', methods=['GET', 'POST'])
def redirect_view(short):
    url = models.URLS.query.filter_by(ShortURL=short).first()
    location = ''
    if url is not None:
        location = url.LongURL
        url.Visits = url.Visits + 1
        ip_address = request.remote_addr

        ip = models.IPS.query.filter_by(address=ip_address).first()
        if ip is not None:
            ips = url.ips
            temp_ids = []
            for i in ips:
                temp_ids.append(i.id)

            if ip.id in ips:  # 已经是相关联的ip
                pass
            else:
                url.ips.append(ip)
                db.session.add(ip)
                db.session.commit()
        else:
            ip = models.IPS(address=ip_address)
            url.ips.append(ip)
            db.session.add(ip)
            db.session.commit()

        db.session.commit()
    else:
        abort(404)
    return redirect(location, code=302)


@main.route('/generate_auth_token/', methods=['GET'])
@login_required
def generate_auth_token():
    user_id = session['user_id']
    jsondata = {}
    user = models.USERS.query.get(user_id)
    expires_time = timedelta(weeks=0, days=1, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0, )
    access_token = create_access_token(identity=user_id, expires_delta=expires_time)

    jsondata['auth_token'] = access_token
    return jsonify(jsondata)


@main.route('/get_statistical_data/', methods=['GET'])
@login_required
def get_statistical_data():
    user_id = session['user_id']
    jsondata = []
    # 这个用户的链接
    URLS = models.URLS.query.filter_by(user_id=user_id)
    for i in URLS:
        temp = {}
        temp['short'] = i.Location
        temp['long'] = i.LongURL
        temp['visits'] = i.Visits
        ipcount = 0
        for j in i.ips:
            ipcount += 1
        temp['ipcounts'] = ipcount
        jsondata.append(temp)

    return jsonify(jsondata)
