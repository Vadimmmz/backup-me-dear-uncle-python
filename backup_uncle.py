from tkinter import Label, Button, Entry, Text, IntVar, Tk, W, Checkbutton, Toplevel, Message
from tkinter import Menu
from tkinter.ttk import Combobox
import time
from functions.lang_module import define_language, set_language
from functions.ui_functions import open_about, open_help, close_program, open_root_folder, open_destination_folder
from functions.service_functions import read_patches_from_file
from functions.create_backup import backup_process
import threading
from google_connect import google_auth, google_sign_in, google_sign_out


class Interface:
    def __init__(self, tkinter_obj):
        self.g_auth = None
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

        test_text = "Test Text... \n Trolo lo lo lo Lo Lo Lo Trooooloooolooo oho ho ho ho" \
                    "yp ho ho hohooooo oho ho ho hoooo ohoho hotrololoooo looooou loo lo"

        # Message label border
        empty_text_for_border = 5 * ((165 * "\xa0") + "\n")
        self.message_label_border = Label(tkinter_obj, text=empty_text_for_border, borderwidth=2, relief='groove')
        self.message_label_border.place(x=12, y=290)

        # Message label
        self.message_label = Label(tkinter_obj, text='', wraplength=490, foreground='green')
        self.message_label.place(x=20, y=300)

        self.button_create_bckp = Button(tkinter_obj, text=self.txt_lng['button_create_bckp'],
                                         command=lambda: threading.Thread(target=lambda: backup_process(self)).start())
        self.button_create_bckp.grid(row=11, column=0, sticky=W, pady=10, padx=10)

        # Check buttons
        self.enabled = IntVar()
        self.openfolder_checkbutton = Checkbutton(text=self.txt_lng['openfolder_checkbutton'], variable=self.enabled)
        self.openfolder_checkbutton.place(x=6, y=260)

        self.enabled_google = IntVar()
        self.google_checkbutton = Checkbutton(text=self.txt_lng['google_load'], variable=self.enabled_google)
        self.google_checkbutton.place(x=290, y=260)

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

        self.settings_menu.add_command(label=self.txt_lng['settings_menu_google'],
                                       command=lambda: self.auth_window_open())
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

    def auth_window_open(self):
        self.auth_window = Toplevel(self.tkinter_obj)
        self.auth_window.protocol('WM_DELETE_WINDOW', lambda: self.close_auth_window())
        self.auth_window.title(self.txt_lng['auth_window_title'])
        self.auth_window.resizable(False, False)
        self.auth_window.geometry(f'450x220+400+250')
        self.auth_window.iconbitmap('app_data/uncle_icon.ico')
        self.auth_window.wm_attributes('-topmost', True)
        self.tkinter_obj.wm_attributes('-disabled', True)
        # Makes main app window unactive while settings window is open
        # self.auth_window.overrideredirect(True)

        self.auth_text1 = Message(self.auth_window, width=400,
                                  text='Авторизуйтесь в Google Drive ,чтобы иметь возможность '
                                       'сохранять ваши резервные копии в своем облачном хранилище.', )
        self.auth_text1.grid(row=0, column=0, padx=10)

        self.button_get_psw = Button(self.auth_window, text='Получить код', command=lambda: google_auth(self))
        self.button_get_psw.grid(row=1, column=0, pady=10)

        self.auth_text2 = Label(self.auth_window, text='Введите полученный код доступа:')
        self.auth_text2.place(x=14, y=85)

        self.auth_secret = Entry(self.auth_window, width=60, borderwidth=1)
        self.auth_secret.place(x=14, y=110)

        self.button_auth = Button(self.auth_window, text='Войти', command=lambda: google_sign_in(self))
        self.button_auth.place(x=390, y=105)

        self.button_auth_out = Button(self.auth_window, text='Выйти из аккаунта', command=google_sign_out)
        self.button_auth_out.place(x=14, y=145)

        button_close_auth_window = Button(self.auth_window, text='Закрыть окно',
                                          command=lambda: self.close_auth_window())
        button_close_auth_window.place(x=14, y=180)


    def close_auth_window(self):
        self.tkinter_obj.wm_attributes('-disabled', False)
        self.auth_window.destroy()

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
            text = f"{self.txt_lng['uploading_text']}   "
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)
            text = f"{self.txt_lng['uploading_text']}.  "
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)
            text = f"{self.txt_lng['uploading_text']}.. "
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)
            text = f"{self.txt_lng['uploading_text']}..."
            self.google_checkbutton.configure(text=text)
            time.sleep(0.5)


window = Tk()
window.title("Backup me, dear uncle Python! (v 1.0)")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2 - 300
h = h // 2 - 200

window.geometry(f'600x420+{w}+{h}')
window.iconbitmap('app_data/uncle_icon.ico')
window.resizable(False, False)

ui = Interface(window)
window.mainloop()
