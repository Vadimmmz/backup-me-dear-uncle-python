from tkinter import Tk
from functions.user_Interface import Interface

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
