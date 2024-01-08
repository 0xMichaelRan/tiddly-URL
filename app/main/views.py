from flask import request, jsonify, abort, redirect, render_template
from .. import db
from . import main
from .. import models
from .. import Change


@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@main.route('/shorten/', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    jsondata = {}

    url = models.URLS.query.filter_by(LongURL=long_url).first()
    if url is not None:
        jsondata['long'] = url.LongURL
        jsondata['short'] = url.ShortURL
    else:
        url = models.URLS(LongURL=long_url)
        db.session.add(url)

        url = models.URLS.query.filter_by(LongURL=long_url).first()
        a = Change.ShortURL()
        short_url = a.encode(url.id)

        url.ShortURL = short_url
        jsondata['long'] = url.LongURL
        jsondata['short'] = url.ShortURL
        db.session.commit()

    return jsonify(jsondata)


@main.route('/lengthen/', methods=['POST'])
def longen():
    short_url = request.form['short_url']
    url = models.URLS.query.filter_by(ShortURL=short_url).first()
    jsondata = {}

    if url is not None:
        a = Change.ShortURL()
        id = a.decode(short_url)
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
