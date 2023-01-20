import googletrans
from googletrans import Translator

print(googletrans.__version__)
print(googletrans.LANGUAGES)
translator = Translator()
text1 = 'おはようございます'
text2 = 'Hello'
language = 'es'
translated = translator.translate(text1, dest=language)
languages = googletrans.LANGUAGES
lang = str(languages[str(translated.src)])

translation: dict = {
            "Source language": languages[str(translated.src)].capitalize(),
            "Translation": str(translated.text),
            "Pronunciation": str(translated.extra_data['origin_pronunciation'])
        }
print(translation)
# for python 3.8 or below
