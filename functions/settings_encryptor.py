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


class Encryptor:
    """
        This class let avoid accidentally double encrypt.

    """
    def __init__(self):
        self.encrypted = True

        # Change value of this variable if you need change the path for settings.yaml (or change variable's name)
        self.root_path = get_project_root()
        self.GOOGLE_SETTINGS_PATH = str(self.root_path) + '/app_data/settings.yaml'

    def is_encrypted(self):
        if self.encrypted:
            return True
        else:
            return False

    def encrypt(self):
        if not self.is_encrypted():
            key = self.load_key()

            # Creating Fernet object
            f = Fernet(key)

            with open(self.GOOGLE_SETTINGS_PATH, 'rb') as file:
                # Reading all data from file
                file_data = file.read()

            # Encrypting data
            encrypted_data = f.encrypt(file_data)

            # Writing data to file
            with open(self.GOOGLE_SETTINGS_PATH, 'wb') as file:
                file.write(encrypted_data)

            self.encrypted = True

    def decrypt(self):
        if self.is_encrypted():
            key = self.load_key()

            # Creating Fernet object
            f = Fernet(key)

            with open(self.GOOGLE_SETTINGS_PATH, 'rb') as file:
                # Writing encrypted data
                encrypted_data = file.read()

            # Decrypting data
            decrypted_data = f.decrypt(encrypted_data)

            # Writing data to file
            with open(self.GOOGLE_SETTINGS_PATH, 'wb') as file:
                file.write(decrypted_data)

            self.encrypted = False

    def write_key(self):
        """
            Use this function for make you own secret key for encrypt/descrypt settings.yaml file

        """

        key = Fernet.generate_key()
        #key = 'place your key here if you want to compile this app'

        with open('app_data/crypto.key', 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        # Creating crypto.key file if it not exists
        if not os.path.exists('app_data/crypto.key'):
            self.write_key()

        return open('app_data/crypto.key', 'rb').read()

    def first_running(self):
        """
            This function is necessary for the initial encryption setup.
        """
        self.write_key()
        self.encrypted = False
        self.encrypt()


# This variable let avoid accidentally double encrypt
encryptor = Encryptor()











