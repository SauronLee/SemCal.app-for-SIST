from flask_restful import Api

from App.apis.common.semcal_api import SemCalsResource

common_api = Api(prefix='/common')
common_api.add_resource(SemCalsResource, '/SemCals/')