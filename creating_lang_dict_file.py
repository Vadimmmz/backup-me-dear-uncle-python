import pickle

ru = {
    'messagebox_title': 'О программе',
    'messagebox_text': f'Backup me, dear uncle Python! (v 1.0) \n'
                       f'Автор программы Зорин Вадим vadimmmz@mail.ru \n'
                       f'Санкт-Петербург 2023',

    'msg_lbl_done': 'Копия создана в директории: ',
    'msg_lbl_choice_fldr': 'Выберите папку для копирования!',
    'msg_lbl_error': 'Ошибка создания резервной копии!\n',

    'lbl_info1': 'Выберите папку, для которой следует сделать резервную копию',
    'lbl_info2': 'Выберите папку, куда будем сохранять резервную копию',
    'lbl_name': 'Введите имя для файла архива (необязательно):',
    'lbl_comment_field': 'Напишите комментарий, для info.txt внутри архива(необязательно):',

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

    'mainmenu_setting': 'Настройки',
    'mainmenu_help': 'Справка',

    'loading_text': 'Резервная копия создается'
}

eng = {
    'messagebox_title': 'About',
    'messagebox_text': f'Backup me, dear uncle Python! (v 1.0) \n'
                       f'Made by Vadim Zorin vadimmmz@mail.ru \n'
                       f'Saint-Petersburg 2023',

    'msg_lbl_done': 'Copy created in directory: ',
    'msg_lbl_choice_fldr': 'To create a backup copy, select the necessary directories!',
    'msg_lbl_error': 'Backup creation error!\n',

    'lbl_info1': 'Select the folder for which you want to make a backup',
    'lbl_info2': 'Select the folder where we will save the backup',
    'lbl_name': 'Enter a name for the archive file (optional):',
    'lbl_comment_field': 'Write a comment for info.txt inside the archive (optional):',

    'button_select': ' Select ',
    'button_create_bckp': 'Create a backup',

    'openfolder_checkbutton': 'Open the folder with the file after it is created.',
    'google_load': 'Upload to Google Drive',

    'helpmenu_help': 'Help',
    'helpmenu_about': 'About',

    'settings_menu_language_ru': 'Russian',
    'settings_menu_language_en': 'English',

    'settings_menu_lang': 'Language',
    'settings_menu_exit': 'Exit',

    'mainmenu_setting': 'Settings',
    'mainmenu_help': 'Help',

    'loading_text': 'A backup is being created'
}

languages = {'russian': ru, 'english': eng}
languages_file = 'app_data/language.data'

# Creating 'language.data' file
f = open(languages_file, 'wb')
pickle.dump(languages, f)
f.close()





