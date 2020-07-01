from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel
from App.models.semcal_user.model_constant import PERMISSION_NONE

BLACK_USER = 1
COMMON_USER = 2
VIP_USER = 4

class SemCalUser(BaseModel):
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    is_delete = db.Column(db.Boolean, default=False)
    permissiomn = db.Column(db.Integer, default=PERMISSION_NONE)

    @property
    def password(self):
        raise Exception("can't access")
    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)

    def check_permission(self, permission):

        if BLACK_USER & permission == BLACK_USER:
            return False
        else:
            return permission & self.permissiomn == permission