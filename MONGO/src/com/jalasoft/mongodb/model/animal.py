#
# @users.py Copyright (c) 2022 Jalasoft.
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


class Animal:
    """Defines the user"""
    def __init__(self, percentage,  method, word, file_name, file_path):
    
        self.percentage = percentage
        self.method = method
        self.word = word
        self.file_name = file_name
        self.file_path = file_path
    
    def toDBCollection(self):
        """Gives format for store in data base"""
        return{
           
            'percentage': self.percentage,
            'method': self.method,
            'word': self.word,
            'file_name': self.file_name,
            'file_path': self.file_path
        }
        