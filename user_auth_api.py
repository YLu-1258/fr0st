from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
from user_auth import *

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
auth_api = Blueprint('a_api', __name__,
                   url_prefix='/api/auth')  # endpoint prefix avoid redundantly typing /api/login over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
a_api = Api(auth_api)

class AuthAPI:
    class _ExposeAuth(Resource):
        def get(self):
            return jsonify(getCredentials())

    class _GetPwd(Resource):
        def get(self,usr):
            return jsonify(getPwd(usr))

    class _GetScore(Resource):
        def get(self,usr):
            return jsonify(getHighScore(usr))

    class _GetLeader(Resource):
        def get(self):
            return jsonify(getChampion())

    class _VerifyLogin(Resource):
        def get(self, usr,pwd):
            return jsonify(verifyLogin(usr,pwd))

    class _UpdatePwd(Resource):
        def get(self, usr,pwd):
            setUser(usr,pwd)
            return jsonify(getPwd(usr))  

    class _UpdateScore(Resource):
        def get(self, usr,score):
            setScore(usr,score)
            return jsonify(getHighScore(usr))  

    class _UpdateLeader(Resource):
        def get(self):
            return jsonify(getChampion())  

    class _Register(Resource):
        def get(self,usr,pwd="password"):
            return jsonify(setUser(usr,pwd))

    a_api.add_resource(_ExposeAuth, "/")
    a_api.add_resource(_GetPwd, "/<string:usr>/pwd")
    a_api.add_resource(_GetScore, "/<string:usr>/score")
    a_api.add_resource(_GetLeader, "/champ")
    a_api.add_resource(_VerifyLogin, "/<string:usr>/<string:pwd>/verify")
    a_api.add_resource(_UpdatePwd, "/<string:usr>/<string:pwd>/p_update")
    a_api.add_resource(_UpdateScore, "/<string:usr>/<int:score>/s_update")
    a_api.add_resource(_UpdateLeader, "/leader")
    a_api.add_resource(_Register, "/<string:usr>/<string:pwd>/register")