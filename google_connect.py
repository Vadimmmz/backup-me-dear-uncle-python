from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import webbrowser
import os
from tkinter import messagebox


def google_auth(ui):
    ui.g_auth = GoogleAuth()
    auth_url = ui.g_auth.GetAuthUrl()  # Create authentication url user needs to visit
    webbrowser.open(auth_url)


def google_sign_in(ui):
    try:
        code = ui.auth_secret.get().strip()
        ui.g_auth.Auth(code)
        messagebox.showinfo('Title success!', 'Авторизация прошла успешно!')
    except Exception:
        messagebox.showinfo('Title fail!', 'Авторизация не удалась. Пропробуйте еще раз')


def google_sign_out():
    with open('credentials.json', 'w') as f:
        pass


"""
def connect_google():
    if os.path.exists('credentials.json'):
        g_auth = GoogleAuth()
    else:
        g_auth = GoogleAuth()
        auth_url = g_auth.GetAuthUrl()  # Create authentication url user needs to visit
        code = ask_user(auth_url)  # Your customized authentication flow
        g_auth.Auth(code)

    return g_auth"""


def google_upload(file_name: str, file_path: str, ui):
    try:
        if os.path.exists('credentials.json'):
            g_auth = GoogleAuth()
        else:
            # Make this file and start auth
            assert Exception()

        drive = GoogleDrive(g_auth)

        file_path = file_path + '/' + file_name
        my_file = drive.CreateFile({'title': file_name})
        my_file.SetContentFile(file_path)
        my_file.Upload()
        ui.is_uploading = False
        return ui.txt_lng['uploaded_to_google']

    except Exception as e:
        ui.is_uploading = False
        return f'Something went wrong :(\n {e}'
