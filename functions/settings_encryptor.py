"""

    This module provides safety of your personally google application settings file.
    If you want to make your own standalone version of 'Backup me dear uncle Python'
    you need to modify settings_encryptor.py module and decide how you
    will hide your crypto.key file for secure.

    It's possible to storage data from crypto.key inside some variable right in this module,
    and replace line 'key = load_key()' with 'key = key_for_compile '

"""

from cryptography.fernet import Fernet
import os
from functions.service_functions import get_project_root


# Change value of this variable if you need change the path for settings.yaml (or change variable's name)
root_path = get_project_root()
GOOGLE_SETTINGS_PATH = str(root_path) + '/app_data/settings.yaml'

key_for_compile = 'place your key here if you want to compile this app'


def first_running():
    """
        This function is necessary for the initial encryption setup
    """
    write_key()
    encrypt()


def write_key():
    """
        Use this function for make you own secret key for encrypt/descrypt settings.yaml file

    """

    key = Fernet.generate_key()
    with open('app_data/crypto.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    # Creating crypto.key file if it not exists
    if not os.path.exists('app_data/crypto.key'):
        write_key()

    return open('app_data/crypto.key', 'rb').read()


def encrypt(filename=GOOGLE_SETTINGS_PATH):

    key = load_key()

    # Creating Fernet object
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # Reading all data from file
        file_data = file.read()

    # Encrypting data
    encrypted_data = f.encrypt(file_data)

    # Writing data to file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename=GOOGLE_SETTINGS_PATH):
    key = load_key()

    # Creating Fernet object
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # Writing encrypted data
        encrypted_data = file.read()

    # Decrypting data
    decrypted_data = f.decrypt(encrypted_data)

    # Writing data to file
    with open(filename, 'wb') as file:
        file.write(decrypted_data)
