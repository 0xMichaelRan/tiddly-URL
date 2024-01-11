from functools import wraps
from flask import session, abort


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('login'):
            abort(403)
        return f(*args, **kwargs)

    return wrapper
