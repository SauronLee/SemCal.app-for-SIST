from flask_restful import Resource

from App.apis.admin.utils import login_required


class SemCalsResource(Resource):
    def get(self):
        return {"msg": "get ok"}
    @login_required
    def post(self):
        return {"msg": "post ok"}
