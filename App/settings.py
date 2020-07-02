# -*- coding: utf-8 -*-
import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine,driver,user,password,host,port,name)



class Config:

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY="SIST"
    SESSION_TYPE ="redis"

class DevelopConfig(Config):
    DEBUG = True
    dbinfo={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'debian-sys-maint',
        'PASSWORD':'R4HyrgdJfuzjKnWW',
        'HOST':'localhost',
        'PORT':3306,
        'NAME':'SemCal_User',

    }
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_POST = 25
    MAIL_USERNAME = "chilyoniki@gmail.com"
    MAIL_PASSWORD = "lixiaoran123"
    MAIL_DEFAULT_SENDER_URI = MAIL_USERNAME
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "defualt": DevelopConfig
}

ADMINS = ('Lixiaoran', 'Sauron')
UPLOADS_DIR = '/home/lixiaoran/SemCal/static/uploads/icons/'