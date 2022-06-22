from tkinter import *
import Database
import Thanks
class Question:
    subject = ''
    def __init__(self,root,sub):
        root.destroy()
        self.gui = Tk()
        self.collection = sub
        self.i = 1
        self.answer = 0
        self.score = 0
        self.dict = {}
        self.cnt = 0
        self.dict = Database.show_data(self.collection, Database.myDB, self.i)
        self.dummy = Database.show_data1(self.collection,Database.myDB)
        for i in self.dummy:
            self.cnt += 1
        self.questionPage()

    # it will fetch data from database according to question selected in subject selection interface
    def data(self):
        self.a.config(text = "")
        self.b.config(text="")
        self.c.config(text = "")
        self.d.config(text="")

        if self.var.get() == self.answer: # calculating score
            self.score += 1


        self.i = self.i + 1
        self.dict = Database.show_data(self.collection, Database.myDB, self.i)

        if self.i < self.cnt:
            self.questionPage()
        else:
            if self.collection == "Python_Quiz":
                Question.subject = "Python"
            elif self.collection == "Java_Quiz":
                Question.subject = "Java"
            elif self.collection == "Csharp_Quiz":
                Question.subject = "Csharp"
            Thanks.Thanks(self.gui, self.score)

    # creating question page
    def questionPage(self):
        # self.dict = Database.show_data(self.collection, Database.myDB, self.i)
        self.gui.title("Quiz Application")
        # self.data(1)

        self.var = IntVar()
        self.answer = IntVar()

        #fetching data from dictionary and displaying on interface
        for x in self.dict:
            if x:
            # self.i += 1
                q_no = Label(self.gui, text=f"Q{self.i}:{x['Question']}", width=80, #question number
                                        font=('ariel', 16, 'bold'), anchor='w')
                         # placing the option on the screen
                q_no.place(x=70, y=90)

                self.a = Radiobutton(self.gui, text=f"{x['Option1']}" ,font="calibri 16 bold", variable=self.var, value = 1)#value=hardQ&#91;x]&#91;1],variable = var,
                self.a.place(x=70, y=150, anchor='w')

                self.b = Radiobutton(self.gui,  text=f"{x['Option2']}",font="calibri 16 bold", variable=self.var, value = 2) # &  # 91;x]&#91;2] value=hardQ&#91;x]&#91;2],variable = var,
                self.b.place(x=70, y=200, anchor='w')

                self.c = Radiobutton(self.gui, text=f"{x['Option3']}" ,font="calibri 16 bold", variable=self.var, value = 3) # &  # 91;x]&#91;3] ,value=hardQ&#91;x]&#91;3],variable = varvalue=hardQ&#91;x]&#91;4],variable = var,
                self.c.place(x=70, y=250, anchor='w')

                self.d = Radiobutton(self.gui, text=f"{x['Option4']}" ,font="calibri 16 bold", variable=self.var, value = 4) #&  # 91;x]&#91;4]
                self.d.place(x=70, y=300, anchor='w')
                self.answer =  x['Correct_Answer']

        # next button to go to next question
        self.next = Button(self.gui,text = "Next", padx=5, pady=5, width=5, bg='grey', font=("", 12, "bold"),command = self.data)
        self.next.configure(width=15, height=1, activebackground="#33B5E5", activeforeground="#071bf0", relief=FLAT)
        self.next.place(x=350,y=350)

        self.gui.geometry("1100x450")
        self.gui.mainloop()

