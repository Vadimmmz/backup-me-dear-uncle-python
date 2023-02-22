from tkinter import Label, Button, Entry, Text, IntVar, Tk, W, Checkbutton
from tkinter import Menu
from tkinter.ttk import Combobox
import time
from functions.lang_module import define_language, set_language
from functions.ui_functions import open_about, open_help, close_program, open_root_folder, open_destination_folder
from functions.service_functions import read_patches_from_file
from functions.create_backup import backup_process
import threading


class Interface:
    def __init__(self, tkinter_obj):
        self.is_uploading = False
        self.tkinter_obj = tkinter_obj
        self.is_creating = False
        self.txt_lng, self.lang = define_language()

        # Creating UI widgets
        self.lbl_info1 = Label(tkinter_obj, text=self.txt_lng['lbl_info1'], pady=5)
        self.lbl_info1.grid(row=2, column=0, sticky=W)
        self.root_folder = Combobox(tkinter_obj, width=80)
        self.root_folder.grid(row=3, column=0, padx=10)
        self.button_find = Button(tkinter_obj, text=self.txt_lng['button_select'],
                                  command=lambda: open_root_folder(self))
        self.button_find.grid(row=3, column=1)

        self.lbl_info2 = Label(tkinter_obj, text=self.txt_lng['lbl_info2'])
        self.lbl_info2.grid(row=4, column=0, sticky=W)
        self.destination_folder = Combobox(tkinter_obj, width=80)
        self.destination_folder.grid(row=5, column=0)
        self.button_find_dest = Button(tkinter_obj, text=self.txt_lng['button_select'],
                                       command=lambda: open_destination_folder(self))
        self.button_find_dest.grid(row=5, column=1)

        # Field for Name
        self.lbl_name = Label(tkinter_obj, text=self.txt_lng['lbl_name'])
        self.lbl_name.grid(row=7, column=0, sticky=W)
        self.name_field = Entry(tkinter_obj, width=83, borderwidth=1)
        self.name_field.grid(row=8, column=0, padx=10)

        # Comment field for readme.txt
        self.lbl_comment_field = Label(tkinter_obj, text=self.txt_lng['lbl_comment_field'])
        self.lbl_comment_field.grid(row=9, column=0, sticky=W)
        self.comment_field = Text(tkinter_obj, width=62, height=3)
        self.comment_field.grid(row=10)

        # Message label
        self.message_label = Label(tkinter_obj, text="", wraplength=510, foreground='green')
        self.message_label.grid(row=14, column=0)

        self.button_create_bckp = Button(tkinter_obj, text=self.txt_lng['button_create_bckp'],
                                         command=lambda: threading.Thread(target=lambda: backup_process(self)).start())
        self.button_create_bckp.grid(row=11, column=0, sticky=W, pady=10, padx=10)

        self.enabled = IntVar()
        self.openfolder_checkbutton = Checkbutton(text=self.txt_lng['openfolder_checkbutton'], variable=self.enabled)
        self.openfolder_checkbutton.grid(row=12, column=0, sticky=W, padx=5)

        self.enabled_google = IntVar()
        self.google_checkbutton = Checkbutton(text=self.txt_lng['google_load'], variable=self.enabled_google)
        self.google_checkbutton.grid(row=13, column=0, sticky=W, padx=5)

        # Get last pathes from file path.txt
        self.root_folder['values'] = read_patches_from_file(path_type=self.root_folder,
                                                            file_type='app_data/root_path.txt')
        self.destination_folder['values'] = read_patches_from_file(path_type=self.destination_folder,
                                                                   file_type='app_data/dest_path.txt')

        # Main menu
        self.mainmenu = Menu(tkinter_obj)
        self.tkinter_obj.config(menu=self.mainmenu)

        self.helpmenu = Menu(self.mainmenu, tearoff=0)
        self.helpmenu.add_command(label=self.txt_lng['helpmenu_help'], command=lambda: open_help(self))
        self.helpmenu.add_command(label=self.txt_lng['helpmenu_about'], command=lambda: open_about(self.txt_lng))

        self.settings_menu = Menu(self.mainmenu, tearoff=0)

        self.settings_menu_language = Menu(self.settings_menu, tearoff=0)
        self.settings_menu_language.add_command(label=self.txt_lng['settings_menu_language_ru'],
                                                command=lambda: set_language('r', ui))
        self.settings_menu_language.add_command(label=self.txt_lng['settings_menu_language_en'],
                                                command=lambda: set_language('e', ui))

        self.settings_menu.add_cascade(label=self.txt_lng['settings_menu_lang'],
                                       menu=self.settings_menu_language)
        self.settings_menu.add_command(label=self.txt_lng['settings_menu_exit'],
                                       command=lambda: close_program(tkinter_obj))

        self.mainmenu.add_cascade(label=self.txt_lng['mainmenu_setting'], menu=self.settings_menu)
        self.mainmenu.add_cascade(label=self.txt_lng['mainmenu_help'], menu=self.helpmenu)

    def update(self):
        self.txt_lng, self.lang = define_language()
        self.lbl_name.configure(text=self.txt_lng['lbl_name'])
        self.lbl_info1.configure(text=self.txt_lng['lbl_info1'])
        self.lbl_info2.configure(text=self.txt_lng['lbl_info2'])
        self.button_find.configure(text=self.txt_lng['button_select'])
        self.button_find_dest.configure(text=self.txt_lng['button_select'])
        self.lbl_comment_field.configure(text=self.txt_lng['lbl_comment_field'])
        self.button_create_bckp.configure(text=self.txt_lng['button_create_bckp'])
        self.openfolder_checkbutton.configure(text=self.txt_lng['openfolder_checkbutton'])
        self.google_checkbutton.configure(text=self.txt_lng['google_load'])

        self.mainmenu.destroy()
        self.mainmenu = Menu(self.tkinter_obj)
        self.tkinter_obj.config(menu=self.mainmenu)

        self.helpmenu.destroy()
        self.helpmenu = Menu(self.mainmenu, tearoff=0)
        self.helpmenu.add_command(label=self.txt_lng['helpmenu_help'], command=lambda: open_help(self))
        self.helpmenu.add_command(label=self.txt_lng['helpmenu_about'], command=lambda: open_about(self.txt_lng))

        self.settings_menu.destroy()
        self.settings_menu = Menu(self.mainmenu, tearoff=0)
        self.settings_menu_language = Menu(self.settings_menu, tearoff=0)
        self.settings_menu_language.add_command(label=self.txt_lng['settings_menu_language_ru'],
                                                command=lambda: set_language('r', ui))
        self.settings_menu_language.add_command(label=self.txt_lng['settings_menu_language_en'],
                                                command=lambda: set_language('e', ui))

        self.settings_menu.add_cascade(label=self.txt_lng['settings_menu_lang'],
                                       menu=self.settings_menu_language)
        self.settings_menu.add_command(label=self.txt_lng['settings_menu_exit'],
                                       command=lambda: close_program(window))

        self.mainmenu.add_cascade(label=self.txt_lng['mainmenu_setting'], menu=self.settings_menu)
        self.mainmenu.add_cascade(label=self.txt_lng['mainmenu_help'], menu=self.helpmenu)

    def txt_loader(self, is_creating: bool):
        """

        Animation for text while backup in creating process

        """
        self.is_creating = is_creating
        self.message_label['foreground'] = 'green'
        while self.is_creating is True:
            self.message_label['text'] = f"{self.txt_lng['loading_text']}   "
            time.sleep(0.5)
            self.message_label['text'] = f"{self.txt_lng['loading_text']}.  "
            time.sleep(0.5)
            self.message_label['text'] = f"{self.txt_lng['loading_text']}.. "
            time.sleep(0.5)
            self.message_label['text'] = f"{self.txt_lng['loading_text']}..."
            time.sleep(0.5)

    def txt_loader_google(self, is_uploading: bool):
        """

        Animation for text while backup in Google Drive uploading process

        """
        self.is_uploading = is_uploading
        while self.is_uploading is True:
            text = "Uploading   "
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)
            text = "Uploading.  "
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)
            text = "Uploading.. "
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)
            text = "Uploading..."
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)

window = Tk()
window.title("Backup me, dear uncle Python! (v 1.0)")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2 - 300
h = h // 2 - 200

window.geometry(f'600x400+{w}+{h}')
window.iconbitmap('app_data/uncle_icon.ico')
window.resizable(False, False)

ui = Interface(window)
window.mainloop()
