#
# @image_to_pdf.py Copyright (c) 2021 Jalasoft.
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


class ImageToPDFConvert(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file, lang):
        super().__init__(input_file, output_file)
        self.lang = lang

    def convert(self) -> list:
        """Converts an image with text in a pdf file"""
        command_line = ['tesseract', f'{self.input_file}', f'{self.output_file}', '-l', self.lang, 'pdf']
        return " ".join(command_line)
        