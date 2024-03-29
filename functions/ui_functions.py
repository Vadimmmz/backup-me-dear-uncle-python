"""
    This module consists set of functions which use for UI works.

"""

from tkinter import messagebox, filedialog, END
import os
from functions.service_functions import get_project_root


def open_about(txt_lng: dict):
    messagebox.showinfo(txt_lng['messagebox_title'], txt_lng['messagebox_text'])


def open_help(ui):
    root = get_project_root()
    if ui.lang == 'russian':
        os.startfile(f"{root}/help/help_ru.html")
    elif ui.lang == 'english':
        os.startfile(f"{root}/help/help_en.html")


def open_root_folder(ui):
    root_path = filedialog.askdirectory()
    if root_path:
        ui.root_folder.delete(0, END)
        ui.root_folder.insert(0, root_path)


def open_destination_folder(ui):
    destination_path = filedialog.askdirectory()
    if destination_path:
        ui.destination_folder.delete(0, END)
        ui.destination_folder.insert(0, destination_path)


def close_program(ui):
    ui.destroy()


