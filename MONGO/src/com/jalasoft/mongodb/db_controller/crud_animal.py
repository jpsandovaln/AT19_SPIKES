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
from model.animal import Animal
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
    percentage = request.form['percentage']
    method = request.form['method']
    word = request.form['word']
    file_name = request.form['file_name']
    file_path = request.form['file_path']
    return {
            'percentage': percentage,
            'method': method,
            'word': word,
            'file_name': file_name,
            'file_path': file_path,
            }

            

class CreateAnimal(Resource):
    """Defines Create User class"""
    def post(self):
        """Creates a user"""
        animals = db['animals']
        print("testing a console log------")
        get_animal = get_form_information(request)
        if (get_animal['percentage'] and get_animal["method"] and get_animal["word"]
                and get_animal["file_name"] and get_animal["file_path"]):
            print("creating the object")
            animal = Animal(get_animal['percentage'], get_animal["method"], get_animal["word"], get_animal["file_name"], 
            get_animal["file_path"])
            # find_email = users.find_one({'email': user.email})
            # find_user_name = users.find_one({'user_name': user.user_name})
            # if find_email:
            #     return 'email already used'
            # elif find_user_name:
            #     return 'user already exist'
            print('testint for me:'+ str(URI))
            animals.insert_one(animal.toDBCollection())
            response = {
                            'percentage': get_animal['percentage'],
                            'method': get_animal["method"],
                            'word': get_animal["word"],
                            'file_name': get_animal["file_name"],
                            'file_path': get_animal["file_path"]
                            }
            response = json.dumps(response)
            print(response)
            return response, 200