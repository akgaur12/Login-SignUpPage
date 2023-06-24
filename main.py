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

    
    def lblFrame(self, wn, txt, X, Y, w=220, h=56, enw = 200):
        lf = LabelFrame(wn, text=txt, font=('Microsoft YaHei', 10,), bg="white",)
        lf.place(x=X, y=Y, width=w, height=h,)
        en = Entry(lf, font=('Microsoft YaHei', 12,), bd=0, bg="white")
        en.place(x=10, y=6, width=enw,)
        return en

    
    def loginPage(self):
        f2 = Frame(self.root, )
        f2.place(x=0, y=0, width=1536, height=864)
        
        img1 = PhotoImage(file='bg.png')
        l = Label(f2, image=img1, bd=0,)
        l.image_names = img1
        l.place(x=0, y=0)

        f2 = Frame(f2, bg='#ffffff')
        f2.place(x=503, y=90, width=530, height=580)

        img1 = PhotoImage(file='img1.png')
        lbl = Label(f2, image=img1, bg='#ffffff', bd=0,)
        lbl.image_names = img1
        lbl.place(x=215, y=48,)
        Label(f2, text='Login', font=("Microsoft YaHei", 18), bg='white', fg='brown').place(x=240, y=160)

        self.username = StringVar()
        en_username = self.lblFrame(f2, txt="Username (Email)", X=140, Y=225, w=260, enw=245)
        en_username.config(textvariable=self.username)

        self.user_pass = StringVar()
        en_userpass = self.lblFrame(f2, txt="Password", X=140, Y=300, w=260, enw=245)
        en_userpass.config(textvariable=self.user_pass, show="*")

        btn_resetpass = Button(f2, text='Forgot Password?', font=("Microsoft YaHei", 10), cursor='hand2', bd=0, relief='flat', bg='#ffffff', fg='red', activebackground='white', command=self.reset_password_page)
        btn_resetpass.place(x=140,y=360)

        btn = Button(f2, text='Login', font=("Microsoft YaHei", 14), bg="green", fg='white', bd=1, relief='flat', command=self.login)
        btn.place(x=212,y=416, width=125, height=40)

        Label(f2, text='Create Account.', font=("Microsoft YaHei", 11), bg='#ffffff' ).place(x=175,y=480)

        btn2 = Button(f2, text='SignUp', font=("Microsoft YaHei", 11), cursor='hand2', bd=0, bg='#ffffff', fg='blue', activebackground='#ffffff', activeforeground='green', relief='flat', command=self.home)
        btn2.place(x=305,y=478,)

    
    def otp(self):
        self.otp = str(randint(10000, 99999))
        msg = 'Hello, your OTP is '+str(self.otp)
        Sender = 'emailid@gmail.com' # WRITE YOUR EMAIL ID HERE
        Receiver =  self.user_email.get()

        message = EmailMessage()
        message.set_content(msg)
        message['Subject'] = "Resistration Confirmation"
        message['From'] = Sender
        message['To'] = Receiver

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(Sender,'GENERATE 6-digit random number FROM EMAIL SETTING')
            #server.sendmail(Sender, Receiver, msg)
            server.send_message(message)
            server.quit()
        except Exception:
            messagebox.showerror('Email','Invalid Email ID')

    
    def reg(self):
        fn = self.fname.get()
        ln = self.lname.get()
        e = self.user_email.get()
        p = self.password.get()
        cp = self.cpassword.get()
        ph = self.phone.get()

        if self.check.get()==1:
            if fn!='' or ln!='' or p!='' or cp!='' or ph!='':
                if p==cp: 
                    if self.otp==self.user_otp.get():
                        try:
                            db = sqlite3.connect("User2.db")
                            cr = db.cursor()
                            cr.execute("INSERT INTO info VALUES('"+fn+"', '"+ln+"', '"+p+"', '"+ph+"', '"+e+"')")
                            db.commit()
                            db.close()
                            messagebox.showinfo('Sign Up', 'Account Created Successfully')
                            
                            self.fname.set('')
                            self.lname.set('')
                            self.user_email.set('')
                            self.password.set('')
                            self.cpassword.set('')
                            self.user_otp.set('')
                            self.phone.set('')
                            self.ck_box.deselect()
                        except sqlite3.IntegrityError:
                            messagebox.showwarning('Sign Up', 'Account Already Exists')
                    else:
                        messagebox.showerror('OTP', 'Enter Wrong OTP')
                else:
                    messagebox.showerror('Sign Up', 'Password does not Match')
            else:
                messagebox.showwarning('Sign Up', 'Fill all Entries')
        else:
            messagebox.showwarning('CheckBox', 'Please Agree Terms and Conditions')

    def login(self): 
        n = self.username.get()
        p = self.user_pass.get()

        if n!='' and p!='':
            db = sqlite3.connect("User2.db")
            cr = db.cursor()
            r = cr.execute("SELECT * FROM info WHERE email=='"+n+"' AND password=='"+p+"'")
            
            for i in r:
                messagebox.showinfo('Login', 'Login Successfully')
                self.username.set('')
                break
            else:
                messagebox.showerror('Login', 'Invalid Login id and Password')

            self.user_pass.set('')
            db.close()
        else:
            messagebox.showwarning('Login', 'Please Enter Email and Password')




