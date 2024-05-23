from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion
from flask_cors import CORS
import logging

appl = connexion.FlaskApp(__name__)
# Read the swagger.yml file to configure the endpoints
appl.add_api("swagger.yaml")
app = appl.app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@192.168.44.137:3306/openapi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
