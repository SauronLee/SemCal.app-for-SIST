# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 23:50:37 2020

@author: sauron
"""
import uuid

from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_REGISTER, USER_ACTION_LOGIN, HTTP_OK
from App.apis.semcal_user.semcal_utils import get_user
from App.models.semcal_user import SemCalUser
from App.ext import cache

parse_base = reqparse.RequestParser()
parse_base.add_argument("password", type=str, required=True, help="please nenter password")
parse_base.add_argument("action", type=str, required=True, help="please confirm, the request parameters action")
parse_base.add_argument("username", type=str, required=True, help="please nenter username")

#parse_register = parse_base.copy()
#parse_register.add_argument("username", type=str, required=True, help="please nenter username")

#parse_login = parse_base.copy()
#parse_login.add_argument("username", type=str, required=True, help="please nenter username")

semcal_user_fields = {
    "username": fields.String,
    "password": fields.String(attribute="_password")
}
single_semcal_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(semcal_user_fields)
}


class SemCalUsersResource(Resource):
    
    def post(self):

        args = parse_base.parse_args()

        username = args.get("username")
        password = args.get("password")
        action = args.get("action").lower()

        if action == USER_ACTION_REGISTER:
            #args_register = parse_base.parse_args()
            #username = args_register.get("username")

            semcal_user = SemCalUser()
            semcal_user.username = username
            semcal_user.password = password

            if not semcal_user.save():
                abort(400, msg="create fail")

            data = {
                "status": HTTP_CREATE_OK,
                "msg":"user created successfully",
                "data": semcal_user
            }

            return marshal(data, single_semcal_user_fields)
        elif action == USER_ACTION_LOGIN:

            #args_login = parse_login.parse_args()
            #username = args_login.get("username")

            user = get_user(username)

            if not user:
                print("user =", user)
                abort(400, msg="user not exist(1)",)
            if not user.check_password(password):
                abort(401, msg="password error")
            if user.is_delete:
                abort(401, msg="user not exist")
            token = uuid.uuid4().hex

            cache.set(token, user.id, timeout=60*60*24*7)

            data = {
                "msg" : "login success",
                "status" : HTTP_OK,
                "token" : token
            }

            return data


        else:
            abort(400, msg="please provide correct parameters")
