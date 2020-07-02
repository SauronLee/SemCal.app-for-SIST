from flask_restful import Resource


class SemCalsResource(Resource):
    def get(self):
        return {"msg": "get ok"}
    def post(self):
        return {"msg": "post ok"}
