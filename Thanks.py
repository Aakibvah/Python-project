from tkinter import *
import Database
import datetime
import loginPage
import MatPltLib
import MatPlotLib2
import  MatPlotLib3
import Questions
import Median
import StandardDeviation
from time import strftime

class Thanks:
    def __init__(self,root,score):
        root.destroy()
        self.gui = Tk()
        self.score = score
        self.create()

    # Quit Application
    def quit(self):
        self.gui.destroy()

    # this methode will call next class to check progress
    def mat(self):
        MatPltLib.Matplotlib().progress()

    def mat2(self):
        MatPlotLib2.Matplotlib_2().connect()

    def mat3(self):
        MatPlotLib3.Matplotlib_3().connect()

    #creating thank you page
    def create(self):
        self.gui.title("Quiz Application")
        x = datetime.datetime.now()
        d = strftime("%x")
        Database.insert_my(loginPage.login.email, {"Time": x, "Score": self.score, "Subject": Questions.Question.subject})
        q_no = Label(self.gui, text=f"Thank You \n Score is : {self.score}", width=80,  # question number
                     font=('ariel', 16, 'bold'),bg = "yellow", fg = "black", anchor='w')
        q_no.place(x=170, y=150)

        #Quit button
        self.quit = Button(self.gui, text='Quit', padx=5, pady=5, width=5, bg='grey',
                           font=("", 12, "bold"), command= self.quit)  # command=addUserToDataBase,
        self.quit.configure(width=5, height=1, activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.quit.place(x=290, y=330)

        #next button
        self.progress = Button(self.gui, text='Check Progress', padx=5, pady=5, width=5, bg='grey',
                         font=("", 12, "bold"), command =self.mat)# command=addUserToDataBase,
        self.progress.configure(width=15, height=1, activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.progress.place(x=400, y=330)

        self.attempts = Button(self.gui, text='Total Attempts', padx=5, pady=5, width=5, bg='grey',
                           font=("", 12, "bold"), command=self.mat2)  # command=addUserToDataBase,
        self.attempts.configure(width=15, height=1, activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.attempts.place(x=400, y=360)

        self.maxScore = Button(self.gui, text='Highest Score', padx=5, pady=5, width=5, bg='grey',
                               font=("", 12, "bold"), command=self.mat3)  # command=addUserToDataBase,
        self.maxScore.configure(width=15, height=1, activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.maxScore.place(x=400, y=390)

        Median.Median()
        StandardDeviation.Deviation()
        self.gui.geometry("800x450")
        self.gui.mainloop()