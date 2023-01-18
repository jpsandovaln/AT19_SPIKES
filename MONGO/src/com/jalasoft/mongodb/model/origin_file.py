#
# @origin_file.py Copyright (c) 2022 Jalasoft.
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


class OriginFile:
    """Defines the origin_file"""
    def __init__(self, name, size):
        self.name = name
        
        self.size = size
    
    def toDBCollection(self):
        """Gives format for store in data base"""
        return{
            'name': self.name,
            'size': self.size,
            
        }
        