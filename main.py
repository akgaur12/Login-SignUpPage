from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from random import randint
from email.message import EmailMessage
import smtplib


class Form:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Page")
        self.root.geometry('600x400+400+90')
        icon = PhotoImage(file="img1.png")
        self.root.iconphoto(False, icon)
        self.home()
        self.root.mainloop()
    




