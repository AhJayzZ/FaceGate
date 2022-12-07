from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion

application = connexion.FlaskApp(__name__)

# Read the swagger.yml file to configure the endpoints
application.add_api("swagger.yaml")
app = application.app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@192.168.44.135:3306/openapi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
