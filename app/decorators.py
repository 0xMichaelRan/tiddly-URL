from functools import wraps
from flask import session, abort, request

from . import db
from .models import URLS


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('login'):
            abort(403)
        return f(*args, **kwargs)

    return wrapper


def visit_count(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        full_url = request.path
        print(user_id,full_url)
        try:
            url = URLS.query.filter_by(Location=full_url).first()
            url.Visits = url.Visits + 1
            db.session.commit()
        except Exception as e:
            pass
        return f(*args, **kwargs)

    return wrapper
