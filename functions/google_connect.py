"""
    This module consist all for work with Google Drive API

"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from functions.settings_encryptor import decrypt, encrypt, GOOGLE_SETTINGS_PATH
import os


def google_sign_in(txt_lng: dict, auth_text_result, auth_window):

    decrypt()

    # This varaible let avoid accidentally double encrypt
    encrypted = False

    with open('app_data/credentials.json', 'w') as f:
        pass
    try:
        g_auth = GoogleAuth(settings_file=GOOGLE_SETTINGS_PATH)
        drive = GoogleDrive(g_auth)

        # Encrypting settings
        encrypt()
        encrypted = True

        # Show auth window above other windows
        auth_window.wm_attributes('-topmost', True)
        auth_window.focus_force()

        auth_text_result.configure(text=txt_lng['auth_window_auth_success'])
        auth_text_result['foreground'] = 'green'

        # Disable topmost after show auth window
        auth_window.wm_attributes('-topmost', False)

    except Exception as e:
        if not encrypted:
            encrypt()

        auth_text_result.configure(text=f"{txt_lng['auth_window_auth_fail']}\n{e}")
        auth_text_result['foreground'] = 'red'


def google_sign_out(txt_lng: dict, auth_text_result):

    if os.path.exists('app_data/credentials.json'):
        os.remove('app_data/credentials.json')

    auth_text_result.configure(text=txt_lng['auth_window_msg_out'])
    auth_text_result['foreground'] = 'green'


def google_upload(file_name: str, file_path: str, ui):

    decrypt()

    # This variable let avoid accidentally double encrypt
    encrypted = False

    try:
        if os.path.exists('app_data/credentials.json'):
            g_auth = GoogleAuth(settings_file=GOOGLE_SETTINGS_PATH)
        else:
            raise Exception(ui.txt_lng['auth_window_exception'])

        drive = GoogleDrive(g_auth)

        encrypt()
        encrypted = True

        file_path = file_path + '/' + file_name
        my_file = drive.CreateFile({'title': file_name})
        my_file.SetContentFile(file_path)
        my_file.Upload()

        # Stop upload animation
        ui.is_uploading = False

        return ui.txt_lng['uploaded_to_google']

    except Exception as e:
        if not encrypted:
            encrypt()

        ui.is_uploading = False
        return f"{ui.txt_lng['auth_window_exception_basic']} {e}"
