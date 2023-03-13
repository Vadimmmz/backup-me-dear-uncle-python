import os

'''

This module provides safety of your personally google application settings file.
If you want to make your own standalone version of 'Backup me dear uncle Python'
you need to write your own secret_encryptor.py module and decide how you
will hide your settings.yaml file for secure. Good luck :)

'''

def get_settings_google_path():
    if os.path.exists('functions/secret_encryptor.py'):
        print('secret file was using')
        from functions.secret_encryptor import encrypt_settings
        encrypted_path = encrypt_settings()
        return encrypted_path

    else:
        # disable checkbutton
        print('use ordinary file')
        return 'app_data/settings.yaml'

settings_google_path = get_settings_google_path()

