#
# @text_translator_cli.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from CONVERTER.src.com.jalasoft.converter.model.converter import Converter
from translate import Translator


class TextTranslatorCli(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> str:
        """Translates text into a language given"""
        translator = Translator(to_lang=self.output_file)
        translated = translator.translate(self.input_file)
        return translated

# Filt el hello world
aux = TextTranslatorCli("Hello Team", "es").convert()
print(aux)
