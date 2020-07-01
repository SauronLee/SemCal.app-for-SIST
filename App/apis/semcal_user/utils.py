from flask import request, g
from flask_restful import abort

from App.apis.semcal_user.semcal_utils import get_user
from App.ext import cache


def login_required(fun):

    def wrapper(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            abort(401, msg="not login")
        user_id = cache.get(token)
        if not user_id:
            abort(401, msg="user not avaliable")
        user = get_user(user_id)
        if not user:
            abort(401, msg="must login")
        g.user = user
        g.auth = token
        return fun(*args, **kwargs)
    return wrapper


def require_permission(permission):
    def require_permission_wrapper(fun):
        def warpper(*args, **kwargs):
            token = request.args.get("token")
            if not token:
                abort(401, msg="not login")
            user_id = cache.get(token)
            if not user_id:
                abort(401, msg="user not avaliable")
            user = get_user(user_id)
            if not user:
                abort(401, msg="must login")
            g.user = user
            g.auth = token

            if not user.check_permission(permission):
                abort(403, msg="user can't access")
            return fun(*args, **kwargs)
        return warpper
    return require_permission_wrapper
