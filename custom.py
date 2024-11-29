from tkinter import *

import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title('hello word')

root.iconbitmap('images.ico')

root.geometry('600x200')
button = customtkinter.CTkButton(root, text="my button")
button.pack(padx=20, pady=20)

root.mainloop()
