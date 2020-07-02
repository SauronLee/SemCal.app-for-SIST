import uuid

SEMCAL_USER = "semcal_user"
ADMIN_USER = "admin_user"
MASTER_USER = "master_user"

def generate_token(prefix):
    token = prefix + uuid.uuid4().hex
    return token

def generate_semcal_user_token():
    return generate_token(SEMCAL_USER)

def generate_admin_user_token():
    return generate_token(ADMIN_USER )

def generate_master_user_token():
    return generate_token(MASTER_USER)