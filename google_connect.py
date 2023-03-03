from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from tkinter import messagebox


def google_sign_in(txt_lng: dict, auth_text_result):

    with open('app_data/credentials.json', 'w') as f:
        pass
    try:
        g_auth = GoogleAuth(settings_file='app_data/settings.yaml')
        drive = GoogleDrive(g_auth)
        drive.GetAbout()
        #messagebox.showinfo(txt_lng['auth_window_title'], txt_lng['auth_window_auth_success'])
        auth_text_result.configure(text=txt_lng['auth_window_auth_success'])
        auth_text_result['foreground'] = 'green'
    except Exception:
        auth_text_result.configure(text=txt_lng['auth_window_auth_fail'])
        auth_text_result['foreground'] = 'red'
        #messagebox.showinfo(txt_lng['auth_window_title'], txt_lng['auth_window_auth_fail'])


def google_sign_out(txt_lng: dict, auth_text_result):
    if os.path.exists('app_data/credentials.json'):
        os.remove('app_data/credentials.json')
    else:
        pass
    auth_text_result.configure(text=txt_lng['auth_window_msg_out'])
    auth_text_result['foreground'] = 'green'
    #messagebox.showinfo(txt_lng['auth_window_title'], txt_lng['auth_window_msg_out'])


def google_upload(file_name: str, file_path: str, ui):
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
        return ui.txt_lng['uploaded_to_google']

    except Exception as e:
        ui.is_uploading = False
        return f"{ui.txt_lng['auth_window_exception_basic']} {e}"
