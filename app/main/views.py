from flask import request, jsonify, abort, redirect, render_template, session, url_for, flash, current_app
import ReadConfig
from .. import db
from . import main
from .. import models
from .. import Change
from ..decorators import login_required

config = ReadConfig.readconfig("/Users/zhoumeng/config.json")
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
        pwdInData = models.USERS.query.filter_by(name=username).first()
        if pwdInData == None:  # 用户不存在
            flash('用户不存在')
        else:
            if pwdInData.PassWord == password:  # 登录成功
                current_app.logger.debug("Log success")
                session['login'] = True
                session['username'] = username
                return redirect(url_for("main.index"))
            else:
                flash('密码错误')
    return render_template('login.html')


@main.route('/logout/')
@login_required
def admin_logout():
    session['login'] = False
    session['username'] = None
    flash('Log out successfully!')
    return redirect(url_for('main.login'))


@main.route('/shorten/', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    jsondata = {}

    url = models.URLS.query.filter_by(LongURL=long_url).first()
    if url is not None:
        jsondata['long'] = url.LongURL
        jsondata['short'] = url.ShortURL
        jsondata['location'] = url.Location

    else:
        url = models.URLS(LongURL=long_url)
        db.session.add(url)

        url = models.URLS.query.filter_by(LongURL=long_url).first()
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
    location = request.form['location']
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
    else:
        abort(404)
    return redirect(location, code=301)
