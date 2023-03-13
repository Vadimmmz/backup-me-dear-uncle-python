import os

'''

This module provides safety of your personally google application settings file.
If you want to make your own standalone version of 'Backup me dear uncle Python'
you need to write your own secret_encryptor.py module and decide how you
will hide your settings.yaml file for secure. Good luck :)

'''

if os.path.exists('secret_encryptor.py'):
    pass
    from secret_encryptor import encrypt_settings

    #settings_google_path = encrypt_settings()

    # Temp decision
    settings_google_path = os.getcwd() + '/app_data/settings.yaml'
else:
    settings_google_path = os.getcwd() + '/app_data/settings.yaml'
