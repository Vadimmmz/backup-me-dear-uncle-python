from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from functions.settings_encryptor import decrypt, encrypt
import os


def google_sign_in(txt_lng: dict, auth_text_result, auth_window):
    decrypt()

    with open('app_data/credentials.json', 'w') as f:
        pass
    try:
        g_auth = GoogleAuth(settings_file='app_data/settings.yaml')
        drive = GoogleDrive(g_auth)
        drive.GetAbout()

        # Show auth window above other windows
        auth_window.wm_attributes('-topmost', True)
        auth_window.focus_force()

        auth_text_result.configure(text=txt_lng['auth_window_auth_success'])
        auth_text_result['foreground'] = 'green'

        # Disable topmost after show auth window
        auth_window.wm_attributes('-topmost', False)

    except Exception as e:
        auth_text_result.configure(text=f"{txt_lng['auth_window_auth_fail']}\n{e}")
        auth_text_result['foreground'] = 'red'

    encrypt()


def google_sign_out(txt_lng: dict, auth_text_result):
    if os.path.exists('app_data/credentials.json'):
        os.remove('app_data/credentials.json')
    else:
        pass
    auth_text_result.configure(text=txt_lng['auth_window_msg_out'])
    auth_text_result['foreground'] = 'green'


def google_upload(file_name: str, file_path: str, ui):
    decrypt()

    try:
        if os.path.exists('app_data/credentials.json'):
            g_auth = GoogleAuth(settings_file='app_data/settings.yaml')
        else:
            raise Exception(ui.txt_lng['auth_window_exception'])

        drive = GoogleDrive(g_auth)

        file_path = file_path + '/' + file_name
        my_file = drive.CreateFile({'title': file_name})
        my_file.SetContentFile(file_path)
        my_file.Upload()
        ui.is_uploading = False

        encrypt()
        return ui.txt_lng['uploaded_to_google']

    except Exception as e:
        ui.is_uploading = False
        encrypt()
        return f"{ui.txt_lng['auth_window_exception_basic']} {e}"
