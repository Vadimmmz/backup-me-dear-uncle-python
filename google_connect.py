from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import webbrowser
import os


def ask_user(auth_url):
    webbrowser.open(auth_url)
    print('Enter the password')
    psw = input()
    with open('code_file', 'w', encoding='utf8') as f:
        f.write(psw)
    return psw


def connect_google():
    if os.path.exists('code_file'):
        g_auth = GoogleAuth()
    else:
        g_auth = GoogleAuth()
        auth_url = g_auth.GetAuthUrl()  # Create authentication url user needs to visit
        code = ask_user(auth_url)  # Your customized authentication flow
        g_auth.Auth(code)

    return g_auth


def create_and_upload_file(file_content, file_name='text.txt', ):
    try:
        con = connect_google()
        drive = GoogleDrive(con)

        my_file = drive.CreateFile({'title': file_name})
        my_file.SetContentFile(file_content)
        my_file.Upload()
        return f'File {file_name} loading was done!'

    except Exception as e:
        return f'Something went wrong :(\n {e}'


print(create_and_upload_file(file_content='test_data.txt'))

