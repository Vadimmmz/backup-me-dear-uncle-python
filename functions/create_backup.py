import os
import time
import threading
import shutil
from shutil import make_archive
from tkinter import END
from functions.service_functions import make_copy_dir
from functions.service_functions import read_patches_from_file, write_patches_to_file
from google_connect import google_upload


def create_backup(path: str, path_to_destination: str, name_prefix: str,
                  ui_checkbox_value: int, comment_text: str) -> (str, str):
    """

    This function created zip file which consist backup data, and put _readme.txt into this archive

    """

    try:
        # Make destination directory if this is not exists
        make_copy_dir(path_to_destination)

        if path != '' and path_to_destination != '':

            # Filename constructing
            if name_prefix == "":
                name_sys = time.strftime('%d-%B-%Y_%H-%M-%S')
            else:
                name_prefix = name_prefix.strip()
                name_prefix = name_prefix.replace(" ", '_')
                name_sys = name_prefix + '(' + time.strftime('%d-%B-%Y_%H-%M-%S') + ')'

            # Creating and copy readme file if there is any comment-text for backup

            if comment_text != '':
                with open('_backup_readme.txt', 'w', -1, 'utf-8') as f:
                    f.write(comment_text)
                f.close()
                comment_path = os.getcwd() + os.sep + '_backup_readme.txt'
                shutil.copy(comment_path, path)

            # Backup file name constructing
            name = name_sys

            # create a zip-file
            make_archive(name, 'zip', path, base_dir='.')

            copy_from = os.getcwd() + os.sep + name + '.zip'
            copy_to = path_to_destination + '/' + name + '.zip'

            # Copy zip-file in destination folder
            shutil.copy(copy_from, copy_to)

            # Remove temp files and directories:
            os.remove(copy_from)

            # remove '_backup_readme.txt' from 'path' folder
            if comment_text != '':
                os.remove(comment_path)
                bckp_to_rmv = path + os.sep + '_backup_readme.txt'
                os.remove(bckp_to_rmv)

            if ui_checkbox_value == 1:
                os.startfile(path_to_destination)

            return 'was_created', copy_to, name + '.zip'

        else:
            return 'wasnt_created', None, None

    except Exception as e:
        return 'exception', str(e), None


def backup_process(ui):
    """

    This function is running in thread and complete service actions which necessary for backup creating.

    """

    # Disable UI items till backup is creating
    ui.button_create_bckp['state'] = 'disabled'
    ui.mainmenu.entryconfigure(1, state='disabled')
    ui.mainmenu.entryconfigure(5, state='disabled')

    # Running ui.txt_loader foo, which doing animated text while loading
    threading.Thread(target=lambda: ui.txt_loader(is_creating=True)).start()

    path = ui.root_folder.get().strip()
    path_to_destination = ui.destination_folder.get().strip()
    name_prefix = ui.name_field.get()
    ui_checkbox_value = ui.enabled.get()
    comment_text = ui.comment_field.get(1.0, END).strip()

    backup_result, message, filename = create_backup(path, path_to_destination, name_prefix,
                                                     ui_checkbox_value, comment_text)

    # Stop text animation
    ui.is_creating = False
    time.sleep(2)

    if backup_result == 'was_created':
        # Update last used pathes in file path.txt
        write_patches_to_file(path=path, values=ui.root_folder['values'],
                              file_type='app_data/root_path.txt')

        write_patches_to_file(path=path_to_destination, values=ui.destination_folder['values'],
                              file_type='app_data/dest_path.txt')

        # Reload combobox menu information
        ui.root_folder['values'] = read_patches_from_file(path_type=ui.root_folder,
                                                          file_type='app_data/root_path.txt')

        ui.destination_folder['values'] = read_patches_from_file(path_type=ui.destination_folder,
                                                                 file_type='app_data/dest_path.txt')

        ui.message_label['text'] = ui.txt_lng['msg_lbl_done'] + message + (2 * '\n')
        ui.message_label['foreground'] = 'green'

    elif backup_result == 'wasnt_created':
        ui.message_label['text'] = ui.txt_lng['msg_lbl_choice_fldr']
        ui.message_label['foreground'] = 'red'
    else:
        ui.message_label['text'] = ui.txt_lng['msg_lbl_error'] + message
        ui.message_label['foreground'] = 'red'

    # Delete file '_backup_readme.txt' if it's in root folder
    if os.path.exists('_backup_readme.txt'):
        os.remove('_backup_readme.txt')

    # Upload file on the Google Drive
    ui_checkbox_google_value = ui.enabled_google.get()
    if backup_result == 'was_created' and ui_checkbox_google_value == 1:
        threading.Thread(target=lambda: ui.txt_loader_google(is_uploading=True)).start()
        upload_text = google_upload(file_name=filename, file_path=path_to_destination, ui=ui)
    else:
        upload_text = ''

    # Wait for animation finish
    time.sleep(2)

    # Enable UI items
    ui.message_label['text'] = f"{ui.message_label['text']} {upload_text}"
    ui.google_checkbutton.configure(text=ui.txt_lng['google_load'])
    ui.button_create_bckp['state'] = 'active'
    ui.mainmenu.entryconfigure(1, state='normal')
    ui.mainmenu.entryconfigure(5, state='normal')