
from App.models.admin.admin_user_model import AdminUser


def get_admin_user(user_ident: object) -> object:

    if not user_ident:
        return None

    print("user_ident =", user_ident)
    user = AdminUser.query.get(user_ident)
    print("get_user =", user)

    if user:
        return user

    user = AdminUser.query.filter(AdminUser.username == user_ident).first()

    if user:
        return user

    return None