#
# @image_resize.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from model.converter import Converter


class ImageResize(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file, new_size):
        super().__init__(input_file, output_file)
        self.new_size = new_size

    def convert(self) -> list:
        """ Resizes image to a given % or values, returns the command line"""
        command_line = ['magick', f'{self.input_file}', '-resize', f'{self.new_size}', f'{self.output_file}']
        return " ".join(command_line)
