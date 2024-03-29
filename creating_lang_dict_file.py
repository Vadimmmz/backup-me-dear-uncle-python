"""
    This script necessity for compiling 'language.data' file which store all text data.

    For adding new language just add new variable that consist dictionary and edit
    the 'languages' variable.

    After making of new language dictionary just run this script.

"""

import pickle

ru = {
    'auth_window_title': 'Авторизация в Google Drive',
    'auth_window_label_1': 'Авторизуйтесь в Google Drive ,чтобы иметь возможность '
                           'сохранять ваши резервные копии в своем облачном хранилище.',
    'auth_window_sing_in': 'Войти в аккаунт',
    'auth_window_sing_out': 'Выйти из аккаунта',
    'auth_window_exception_basic': 'Что то пошло не так :(\n',
    'auth_window_exception': 'Авторизуйтесь для загрузки на диск',
    'auth_window_msg_out': 'Вы вышли из профиля',
    'auth_window_auth_success': 'Авторизация прошла успешно!',
    'auth_window_auth_fail': 'Авторизация не удалась. Пропробуйте еще раз',


    'messagebox_title': 'О программе',
    'messagebox_text': f'Backup me, dear uncle Python! (v 1.0) \n'
                       f'Автор программы Зорин Вадим vadimmmz@mail.ru \n'
                       f'Санкт-Петербург 2023 \n'
                       f'https://github.com/Vadimmmz/backup-me-dear-uncle-python',

    'msg_lbl_done': 'Копия создана в директории: ',
    'msg_lbl_choice_fldr': 'Выберите папку для копирования!',
    'msg_lbl_error': 'Ошибка создания резервной копии!\n',

    'lbl_info1': 'Выберите папку, для которой следует сделать резервную копию',
    'lbl_info2': 'Выберите папку, куда будем сохранять резервную копию',
    'lbl_name': 'Введите имя для файла архива (необязательно):',
    'lbl_comment_field': 'Напишите комментарий, для _readme.txt внутри архива(необязательно):',

    'button_select': 'Выбрать',
    'button_create_bckp': 'Создать резервную копию',

    'openfolder_checkbutton': 'Открыть папку с файлом, после его создания.',
    'google_load': 'Загрузить на Google Drive',

    'helpmenu_help': 'Помощь',
    'helpmenu_about': 'О программе',

    'settings_menu_language_ru': 'Русский',
    'settings_menu_language_en': 'English',

    'settings_menu_lang': 'Язык',
    'settings_menu_exit': 'Выход',
    'settings_menu_google': 'Google Drive',

    'mainmenu_setting': 'Настройки',
    'mainmenu_help': 'Справка',

    'loading_text': 'Резервная копия создается',
    'uploaded_to_google': 'Загрузка на Google Drive завершена!',
    'uploading_text': 'Загрузка'
}

eng = {
    'auth_window_title': 'Google Drive authorization',
    'auth_window_label_1': 'Log in to Google Drive to be able to save your backups to your cloud storage',
    'auth_window_sing_in': 'Sign in',
    'auth_window_sing_out': 'Sign out',
    'auth_window_exception_basic': 'Something went wrong :(\n',
    'auth_window_exception': 'Log in to upload to disk',
    'auth_window_msg_out': 'You have logged out of your profile',
    'auth_window_auth_success': 'Authorization was successful!',
    'auth_window_auth_fail': 'Authorization failed. Try again',

    'messagebox_title': 'About',
    'messagebox_text': f'Backup me, dear uncle Python! (v 1.0) \n'
                       f'Made by Vadim Zorin vadimmmz@mail.ru \n'
                       f'Saint-Petersburg 2023 \n'
                       f'https://github.com/Vadimmmz/backup-me-dear-uncle-python',

    'msg_lbl_done': 'Copy created in directory: ',
    'msg_lbl_choice_fldr': 'To create a backup copy, select the necessary directories!',
    'msg_lbl_error': 'Backup creation error!\n',

    'lbl_info1': 'Select the folder for which you want to make a backup',
    'lbl_info2': 'Select the folder where we will save the backup',
    'lbl_name': 'Enter a name for the archive file (optional):',
    'lbl_comment_field': 'Write a comment for _readme.txt inside the archive (optional):',

    'button_select': 'Select',
    'button_create_bckp': 'Create a backup',

    'openfolder_checkbutton': 'Open the folder with the file after it is created.',
    'google_load': 'Upload to Google Drive',

    'helpmenu_help': 'Help',
    'helpmenu_about': 'About',

    'settings_menu_language_ru': 'Russian',
    'settings_menu_language_en': 'English',

    'settings_menu_lang': 'Language',
    'settings_menu_exit': 'Exit',
    'settings_menu_google': 'Google Drive',

    'mainmenu_setting': 'Settings',
    'mainmenu_help': 'Help',

    'loading_text': 'A backup is being created',
    'uploaded_to_google': 'Upload to Google Drive is complete!',
    'uploading_text': 'Uploading'
}

languages = {'russian': ru, 'english': eng}
languages_file = 'app_data/language.data'


# Creating 'language.data' file
f = open(languages_file, 'wb')
pickle.dump(languages, f)
f.close()
