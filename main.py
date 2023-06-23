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
    
    def home(self):
        f1 = Frame(self.root, )
        f1.place(x=0, y=0, width=1536, height=864)
        
        img1 = PhotoImage(file='bg.png')
        l = Label(f1, image=img1, bd=0,)
        l.image_names = img1
        l.place(x=0, y=0, )

        img = Image.open("10.png")
        imgr = img.resize((360, 480))
        img2 = ImageTk.PhotoImage(imgr)

        l2 = Label(f1, image=img2, bg='#ffffff', bd=0,)
        l2.image_names = img2
        l2.place(x=200, y=90, width=460, height=600)

        f2= Frame(self.root, bg='white')
        f2.place(x=660, y=90, width=700, height=600)

        Label(f2, text='Create Account', font=('Microsoft YaHei', 20,), bg='#ffffff', fg='blue').pack(pady=(15,0))

        self.fname = StringVar()
        self.lname = StringVar()
        self.password = StringVar()
        self.cpassword = StringVar()
        self.user_email = StringVar()
        self.phone = StringVar()
        self.user_otp = StringVar()
        self.check = IntVar()

        en_fname = self.lblFrame(f2, 'First Name', X=80, Y=110)
        en_lname = self.lblFrame(f2, 'Last Name', X=360, Y=110)
        en_pass = self.lblFrame(f2, 'Password', X=80, Y=190)
        en_cpass = self.lblFrame(f2, 'Confirm Password', X=360, Y=190)
        en_email = self.lblFrame(f2, 'Email', X=80, Y=270, w=340, h=56, enw=320)
        
        btn_otp = Button(f2, text="Get OTP", font=('Microsoft YaHei', 10,), bg='light green', command=self.otp)
        btn_otp.place(x=480, y=285, width=70, height=33)
        
        en_contact = self.lblFrame(f2, 'Contact', X=80, Y=350)
        en_otp = self.lblFrame(f2, 'Enter OTP', X=360, Y=350)

        en_fname.config(textvariable=self.fname)
        en_lname.config(textvariable=self.lname)
        en_pass.config(textvariable=self.password)
        en_cpass.config(textvariable=self.cpassword, show='*')
        en_email.config(textvariable=self.user_email)
        en_contact.config(textvariable=self.phone)
        en_otp.config(textvariable=self.user_otp)

        self.ck_box = Checkbutton(f2, text='I have read and agree all the terms and conditions.', font=('Microsoft YaHei', 10,), bg='white', variable=self.check)
        self.ck_box.place(x=80, y=425)

        self.btn_reg = Button(f2, text='SignUp', font=("Microsoft YaHei", 14), bg="blue", fg='white', bd=1, relief='flat', command=self.reg)
        self.btn_reg.place(x=280,y=480, width=125, height=40)

        Label(f2, text='I have an account?', font=("Microsoft YaHei", 11), bg='#ffffff' ).place(x=245,y=540)

        btn_login = Button(f2, text='Login', font=("Microsoft YaHei", 11), cursor='hand2', bd=0, bg='#ffffff', fg='blue', activebackground='#ffffff', activeforeground='green', relief='flat', command=self.loginPage)
        btn_login.place(x=382,y=538,)

        



