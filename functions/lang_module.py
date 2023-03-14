"""
    This module provides all that relation with language in the app.

    * for change any text in the app you need to edit 'creating_lang_dict_file.py'
      which locate in the root application folder.
"""

import pickle
import os


def define_language():
    settings_lng_path = os.getcwd() + '/app_data/language.txt'

    if not os.path.exists(settings_lng_path):
        with open('app_data/language.txt', "w", -1, 'utf-8') as f:
            f.write('english')

    with open('app_data/language.txt', "r", -1, 'utf-8') as f:
        settings_lang = f.readline()

    settings_lang = settings_lang.strip()

    with open('app_data/language.data', 'rb') as f:
        text_dict = pickle.load(f)

    return text_dict[settings_lang], settings_lang


def set_language(lang: str, ui):
    if lang == 'r':
        set_lng = 'russian'
    else:
        set_lng = 'english'
    with open('app_data/language.txt', "w", -1, 'utf-8') as f:
        f.write(set_lng)
    ui.update()
