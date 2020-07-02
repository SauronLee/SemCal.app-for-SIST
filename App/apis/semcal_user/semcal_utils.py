from App.models.semcal_user import SemCalUser


def get_semcal_user(user_ident: object) -> object:

    if not user_ident:
        return None

    print("user_ident =", user_ident)
    user = SemCalUser.query.get(user_ident)
    print("get_user =", user)

    if user:
        return user

    user = SemCalUser.query.filter(SemCalUser.username == user_ident).first()

    if user:
        return user

    return None