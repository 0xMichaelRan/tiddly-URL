from flask import request, jsonify
from . import api
from .. import models, db, Change
from flask_jwt_extended import jwt_required

from ..main.views import BASE_URL


@api.route('/shorten/', methods=['POST'])
@jwt_required
def shorten():
    long_url = request.json.get('long_url')
    jsondata = {}

    url = models.URLS.query.filter_by(LongURL=long_url).first()
    if url is not None:
        data = {}
        data['long'] = url.LongURL
        data['short'] = url.ShortURL
        data['location'] = url.Location
        jsondata['msg'] = '请求成功'
        jsondata['code'] = 0
        jsondata['data'] = data

    else:
        url = models.URLS(LongURL=long_url)
        db.session.add(url)

        url = models.URLS.query.filter_by(LongURL=long_url).first()
        a = Change.ShortURL()
        short_url = a.encode(url.id)

        url.ShortURL = short_url
        url.Location = BASE_URL + short_url
        data = {}
        data['long'] = url.LongURL
        data['short'] = url.ShortURL
        data['location'] = url.Location
        jsondata['msg'] = '请求成功'
        jsondata['code'] = 0
        jsondata['data'] = data

        db.session.commit()

    return jsonify(jsondata)


@api.route('/lengthen/', methods=['POST'])
@jwt_required
def lengenth():
    location = request.json.get("location")
    url = models.URLS.query.filter_by(Location=location).first()
    jsondata = {}

    if url is not None:
        a = Change.ShortURL()
        id = a.decode(url.ShortURL)
        url = models.URLS.query.get(id)
        jsondata['long'] = url.LongURL
        jsondata['msg']='请求成功'
    else:
        jsondata['msg'] = '不存在当前短链接'
    return jsonify(jsondata)
