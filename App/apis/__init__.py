# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 23:50:37 2020

@author: sauron
"""
from App.apis.admin import admin_api
from App.apis.common import common_api
from App.apis.semcal_admin import master_client_api
from App.apis.semcal_user import client_api


def init_api(app):
    client_api.init_app(app)
    master_client_api.init_app(app)
    admin_api.init_app(app)
    common_api.init_app(app)