from flask_restful import Api

from App.apis.common.semcal_api import SemCalsResource, SemCalResource

common_api = Api(prefix='/common')
common_api.add_resource(SemCalsResource, '/SemCals/')
common_api.add_resource(SemCalResource, '/SemCals/<int:id>/')