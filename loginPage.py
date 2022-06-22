from tkinter import *
import Database
from SubjectSelection import SubjectSelection
class login:
    email = ''

    def __init__(self,sroot):
        sroot.destroy()
        self. root = Tk()
        self.uname = ""
        self.password = ""
        self.email = ""
        self.create(self.root)

    # this methode will clear entry input after clicking reset button
    def reset(self):  # when reset button will click this function will erase data from entry
        self.user_name_Entry.delete('0', END)
        self.password_Entry.delete('0', END)

    # this methode will fetch email and password from UserDb collection and compare it current
    # input if its true then it will take to next page which is selection of subject.
    # if id or password doesn't match it will show invalid credentials message on label
    def fetchdata(self):
        mail=self.uname.get()
        login.email =mail
        pass1=self.password.get()
        query = {'Email': mail,  'Password': pass1}
        c = Database.search_data('User_Db', query)
        if(c==1):
            # print("Login SuccessFully")
            SubjectSelection(self.root)
        else:
            self.disp.place(x=310, y=250)
        return  mail

    # this methode will Quit the application
    def quit(self):
        self.root.destroy()

    # creating login page interface
    def create(self,root):
        root.title("Quiz Application")
        title = Label(root, text="Login Page", width=50, bg="Yellow", fg="Black", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

        # user label and entry
        self.username_label = Label(root,text="Email:", font=("", 15, "bold"))  # username label
        self.username_label.place(x=200, y=90)

        uname=StringVar()
        self.uname=StringVar()
        self.user_name_Entry = Entry(root, font=("ariel", 10, "bold"),textvariable=self.uname)  # username textbox
        self.user_name_Entry.place(x=315, y=92, width=170, height=30)

        # password label and entry
        self.password_label = Label(root,text="Password:", font=("", 15, "bold") )  # Password label
        self.password_label.place(x=200, y=150)

        password=StringVar()
        self.password=StringVar()
        self.password_Entry = Entry(root, font=("ariel", 10, "bold"),show='*',textvariable=self.password)  # Password textbox
        self.password_Entry.place(x=315, y=150, width=170, height=30)

        self.disp = Label(self.root,text="Invalid Cridential",font=("", 15, "bold"), fg="red")

        # login page
        self.login_button = Button(root, text="Login", width=7, height=1,  bg="grey", command = self.fetchdata,fg="black", font=("", 12, "bold"))  # login button
        self.login_button.configure(activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.login_button.place(x=400, y=200)

        #rset button
        self.reset_button = Button(root, text="Reset", width=7, height=1, activebackground="#33B5E5", activeforeground="#071bf0", command = self.reset,  bg="grey", fg="black", font=("", 12, "bold"))  # Reset button
        self.reset_button.place(x=315, y=200)

        #quit nutton
        self.quit_button = Button(root, text="Quit", width=7, activeforeground="#f00000", height=1, command = quit, bg="black", fg="white", font=("", 12, "bold"))  # quit button
        self.quit_button.place(x=350, y=300)

        self.root.geometry("800x450")
        self.root.mainloop()
    



