
from flask_restful import Resource, reqparse, abort, marshal, fields, marshal_with
from werkzeug.datastructures import FileStorage

from App.apis.admin.utils import login_required
from App.apis.api_constant import HTTP_CREATE_OK, HTTP_OK
from App.apis.common.utils import filename_transfer
from App.models.common.semcal_model import SemCal

parse = reqparse.RequestParser()
"""
    __tablename__ = 'SemCals'
    showname_model_str = db.Column(db.String(64))
    showname_model_en = db.Column(db.String(128))
    autor = db.Column(db.String(64))
    references = db.Column(db.String(256))
    type = db.Column(db.String(64))
    institute = db.Column(db.String(64))
    language = db.Column(db.String(64))
    accuracy_rate = db.Column(db.Integer, default=0)
    country = db.Column(db.String(64))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(256))
    flag = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)
"""

parse.add_argument("showname_model_str", required=True, help="must supply showname_model_str")
parse.add_argument("showname_model_en", required=True, help="must supply showname_model_en")
parse.add_argument("autor", required=True, help="must supply autor")
parse.add_argument("references", required=True, help="must supply references")
parse.add_argument("type", required=True, help="must supply type")
parse.add_argument("institute", required=True, help="must supply institute")
parse.add_argument("language", required=True, help="must supply language")
parse.add_argument("accuracy_rate", required=True, help="must supply accuracy_rate")
parse.add_argument("country", required=True, help="must supply country")
parse.add_argument("openday", required=True, help="must supply openday")
parse.add_argument("backgroundpicture", type=FileStorage, required=True, help="must supply backgroundpicture", location=['files'])

semcal_fields = {
        "showname_model_str" : fields.String,
        "showname_model_en" : fields.String,
        "autor" : fields.String,
        "references" : fields.String,
        "type" : fields.String,
        "institute" : fields.String,
        "language" : fields.String,
        "accuracy_rate" : fields.Integer,
        "country" : fields.String,
        "openday" : fields.DateTime,
        "backgroundpicture" : fields.String
}

multi_semcal_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(semcal_fields))
}



class SemCalsResource(Resource):
    @marshal_with(multi_semcal_fields)
    def get(self):

        multi_semcal = SemCal.query.all()

        data = {
            "msg": "create success",
            "status": HTTP_OK,
            "data": multi_semcal
        }
        return data
    @login_required
    def post(self):

        args = parse.parse_args()
        showname_model_str = args.get("showname_model_str")
        showname_model_en = args.get("showname_model_en")
        autor = args.get("autor")
        references = args.get("references")
        model_type = args.get("type")
        institute = args.get("institute")
        language = args.get("language")
        accuracy_rate = args.get("accuracy_rate")
        country = args.get("country")
        openday = args.get("openday")
        backgroundpicture = args.get("backgroundpicture")
        #backgroundpicture = request.files.get("backgroundpicture")


        semcal = SemCal()
        semcal.showname_model_en = showname_model_en
        semcal.showname_model_str = showname_model_str
        semcal.autor = autor
        semcal.references = references
        semcal.type = model_type
        semcal.institute = institute
        semcal.language = language
        semcal.accuracy_rate = accuracy_rate
        semcal.country = country
        semcal.openday = openday

        print("type(backgroundpicture)=", type(backgroundpicture))
        print("backgroundpicture=", backgroundpicture)

        file_info = filename_transfer(backgroundpicture.filename)
        filepath = file_info[0]
        backgroundpicture.save(filepath)

        semcal.backgroundpicture = file_info[1]


        if not semcal.save():
            abort(400, msg="can't create semcal")

        data = {
            "msg": "create success",
            "status": HTTP_CREATE_OK,
            "data": marshal(semcal, semcal_fields)
        }

        return data

class SemCalResource(Resource):
    def get(self, id):
        semcal = SemCal.query.get(id)
        if not semcal:
            abort(404, msg="semcal is not exist")
        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": marshal(semcal, semcal_fields)
        }
        return data
    @login_required
    def patch(self, id):
        return {"msg": "post ok"}
    @login_required
    def put(self, id):
        return {"msg": "post ok"}
    @login_required
    def delete(self, id):
        return {"msg": "post ok"}