from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import webbrowser
import os


def ask_user(auth_url):
    webbrowser.open(auth_url)
    print('Enter the password')
    psw = input()
    return psw


def connect_google():
    if os.path.exists('credentials.json'):
        g_auth = GoogleAuth()
    else:
        g_auth = GoogleAuth()
        auth_url = g_auth.GetAuthUrl()  # Create authentication url user needs to visit
        code = ask_user(auth_url)  # Your customized authentication flow
        g_auth.Auth(code)

    return g_auth


def google_upload(file_name: str, file_path: str, ui):
    try:
        con = connect_google()
        drive = GoogleDrive(con)

        file_path = file_path + '/' + file_name
        my_file = drive.CreateFile({'title': file_name})
        my_file.SetContentFile(file_path)
        my_file.Upload()
        ui.is_uploading = False

    except Exception as e:
        return f'Something went wrong :(\n {e}'


#print(google_upload(file_content='test_data.txt'))

