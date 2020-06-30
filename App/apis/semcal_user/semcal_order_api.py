from flask_restful import Resource, reqparse, abort
from App.apis.semcal_user.utils import login_required


class SemCalOrdersResource(Resource):

    @login_required
    def post(self):

        return {"msg": "post order ok"}