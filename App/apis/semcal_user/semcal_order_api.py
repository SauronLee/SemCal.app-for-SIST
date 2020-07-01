from flask import g
from flask_restful import Resource, reqparse, abort
from App.apis.semcal_user.utils import login_required, require_permission
from App.models.semcal_user.semcal_user_model import VIP_USER


class SemCalOrdersResource(Resource):

    @login_required
    def post(self):

        user = g.user
        print(user.username)

        return {"msg": "post order ok"}

class SemCalOrderResource(Resource):

    @require_permission(VIP_USER)
    def put(self, order_id):
        return {"msg": "change succes"}