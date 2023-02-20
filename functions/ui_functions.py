from tkinter import messagebox, filedialog, END
import os
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


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


