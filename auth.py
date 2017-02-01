from functools import wraps
from flask import request, Response
import config
import os

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    user = os.environ.get('APP_USER') or config.APP_USER
    passwd = os.environ.get('APP_PASS') or config.APP_PASS
    return username == user and password == passwd

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
