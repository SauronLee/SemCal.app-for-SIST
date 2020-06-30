from App.models.semcal_user import SemCalUser


def get_user(user_ident):
    print("user_ident =", user_ident)
    user = SemCalUser.query.get(user_ident)
    print("get_user =", user)

    if user:
        return user

    user = SemCalUser.query.filter(SemCalUser.username == user_ident).first()

    if user:
        return user

    return None