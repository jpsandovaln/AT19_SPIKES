#
# @crud_origin_file.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from flask import Flask
from flask import request
from flask_restful import Resource
from flask_pymongo import PyMongo
from model.connection_database import DatabaseConnection
from model.origin_file import OriginFile
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)


load_dotenv()
URI = os.getenv('URI')
app.config['MONGO_URI'] = URI + '/db_users_app'
db = DatabaseConnection(URI).db_connection()

mongo = PyMongo(app)

def get_form_information(request):
    """Gets the data from the form"""
    size = request.form['size']
    return {
            'size': size,
            }


class CreateOriginFile(Resource):
    """Defines Create Origin File class"""
    def post(self):
        """Creates Origin File """
        users = db['origin_files']
        get_origin_file = get_form_information(request)

        if (get_origin_file["size"]):
            content =  request.files['content']
            origin_file = OriginFile(content.filename, get_origin_file["size"])
            #find_email = users.find_one({'email': user.email})
            #find_origin_file_name = get_origin_file.find_one({'name': origin_file.name})
            # if find_email:
            #     return 'email already used'
            #if find_origin_file_name:
            #    return 'origin file already exist'
            #else:
            print('testint for me:'+ str(URI))
            mongo.save_file(content.filename, content)
            users.insert_one(origin_file.toDBCollection())
            response = {
                            'name': origin_file.name,
                            'size': origin_file.size,
                            }
            response = json.dumps(response)
            print(response)
            return response, 200