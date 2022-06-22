import loginPage
from tkinter import *
import Database
import datetime
from time import strftime

class SignUp:
    def __init__(self):
        self.sroot = Tk()
        self.sroot.title("Quiz Application")
        self.fname = StringVar()
        self.email = StringVar()
        self.passW = StringVar()
        self.r_passW = StringVar()
        self.create()

        # masking and unmasking password field
    def show_pass(self):
        if (self.c_val.get() == 1):
            self.pass_Entry.config(show='')
            self.repass_Entry.config(show='')
        else:
            self.pass_Entry.config(show="*")
            self.repass_Entry.config(show="*")

    #this methode will tranfer the contron to login page after clicking Login link
    def gotoLogin(self):
        loginPage.login(self.sroot)

    def createUser(self):
        return self.disp


    # this methode will display label if user is already createed it will print message.
    # if password doesn't match it will print message
    def showlabel(self):
        self.email_l = self.email.get()
        x = datetime.datetime.now()
        d = strftime("%x")

        query = {'Email': self.email_l}
        c = Database.search_data('User_Db', query)
        if c == 1:
            self.display.place(x=500, y=330)
        else:
            pass1 = self.passW.get()
            self.r_pass1 = self.r_passW.get()
            if (pass1 != self.r_pass1):
                self.display1 = Label(self.sroot, font=("ariel", 10, "bold"), text='Password Does Not Match')
                self.display1.place(x=500, y=330)
            else:
                query = {'User_Name': self.fname.get(), 'Email': self.email.get(), 'Password': self.passW.get()}
                Database.insert_my('User_Db', query)
                self.disp = Database.createCollection(self.email_l, {"Time": d, "Score": 0, "Subject": ""},
                                                      Database.myDB)
                self.display1 = Label(self.sroot, font=("ariel", 10, "bold"), text='Account Created Succesfully')

                self.display1.place(x=500, y=330)
                loginPage.login(self.sroot)

    # creating signup page
    def create(self):
        # title label for page
        self.title = Label(self.sroot, text="SignUp Page", width=50, bg="Yellow", fg="Black", font=("ariel", 20, "bold"))
        self.title.place(x=0, y=2)

        # first name label and Entry
        self.flabel_label = Label(self.sroot, text="Full Name:", font=("", 15, "bold"))  # username label
        self.flabel_label.place(x=200, y=90)

        self.fname_Entry = Entry(self.sroot, textvariable=self.fname, font=("ariel", 10, "bold"))  # username textbox
        self.fname_Entry.place(x=315, y=92, width=200, height=30)

        # email = StringVar()
        # user name label and Entry
        self.user_label = Label(self.sroot, text="E-mail:", font=("", 15, "bold"))  # Password label
        self.user_label.place(x=200, y=150)

        self.user_Entry = Entry(self.sroot, font=("ariel", 10, "bold"), textvariable=self.email)  # Password textbox
        self.user_Entry.place(x=315, y=150, width=200, height=30)
        self.dummy_email = self.email.get()

        # paswword label and Entry
        self.pass_label = Label(self.sroot, text="Password:", font=("", 15, "bold"))  # Password label
        self.pass_label.place(x=200, y=210)

        self.pass_Entry = Entry(self.sroot, font=("ariel", 10, "bold"), show='*',textvariable=self.passW)  # Password textbox
        self. pass_Entry.place(x=315, y=208, width=200, height=30)

        # rernter passward
        self.pass_label = Label(self.sroot, text="Re-Enter Password:", font=("", 15, "bold"))  # Password label
        self.pass_label.place(x=100, y=270)

        self.repass_Entry = Entry(self.sroot, font=("ariel", 10, "bold"), show='*',textvariable=self.r_passW)  # Password textbox
        self.repass_Entry.place(x=315, y=270, width=200, height=30)

        # password show check box
        self.checkl = Label(self.sroot, font=("ariel", 10, "bold"), text="Show")
        self.checkl.place(x=550, y=208)

        self.c_val = IntVar(value=0)
        self.checkb = Checkbutton(self.sroot, onvalue=1, offvalu=0, variable=self.c_val, command=self.show_pass)
        self.checkb.place(x=590, y=208)

        # call to odin page disp = False
        self.display = Label(self.sroot, font=("ariel", 10, "bold"), text='User already exist please login')

        # signup BUTTON
        self.sp = Button(self.sroot, text='SignUp', padx=5, pady=5, width=5, bg='grey',
                    font=("", 12, "bold"),command = self.showlabel)  # command=addUserToDataBase,
        self.sp.configure(width=15, height=1, activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.sp.place(x=315, y=330)
        # print(dummy_email)


        # link to login page
        self.log = Button(self.sroot, text='Already have a Account?', padx=5, pady=5, width=5, command=self.gotoLogin, bg="white",
                     fg='blue', font=("", 10, "bold"))
        self.log.configure(width=20, height=1, activebackground="#33B5E5", relief=FLAT)
        self.log.place(x=315, y=390)
        self.sroot.geometry("800x450")
        self.sroot.mainloop()

