from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import webbrowser
import os
from tkinter import messagebox


def google_sign_in():

    with open('credentials.json', 'w') as f:
        pass
    try:
        g_auth = GoogleAuth()
        drive = GoogleDrive(g_auth)
        drive.GetAbout()
        messagebox.showinfo('Title success!', 'Авторизация прошла успешно!')
    except Exception:
        messagebox.showinfo('Title fail!', 'Авторизация не удалась. Пропробуйте еще раз')


def google_sign_out():
    if os.path.exists('credentials.json'):
        os.remove('credentials.json')
    else:
        pass
    messagebox.showinfo('Title success!', 'Вы вышли из профиля!')


def google_upload(file_name: str, file_path: str, ui):
    try:
        if os.path.exists('credentials.json'):
            g_auth = GoogleAuth()
        else:
            assert Exception('Авторизуйтесь!')

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
