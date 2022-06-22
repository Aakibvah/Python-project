from tkinter import *
import  Questions
class SubjectSelection:
    def __init__(self,root,):
        root.destroy()
        self.subroot = Tk()
        self.createPage()

    # selection collection based on subject selection
    def Que(self):
        a = self.var.get()
        if a==1:
            sub = "Python_Quiz"
        elif a ==2:
            sub = "Java_Quiz"
        elif a==3:
            sub = "Csharp_Quiz"

        Questions.Question(self.subroot,sub) # will transfer to next page

    # creating subject selection interface usinf radiobuttons
    def createPage(self):
        self.subroot.title("Quiz Application")
        self.var = IntVar()
        # display label
        title = Label(self.subroot, text="Please! select your Quiz subject......", width=50, bg="Yellow", fg="Black", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

        # Radiobutton name Python
        python = Radiobutton(self.subroot, text="Python",command=self.Que, font="calibri 20 bold", variable=self.var, value=1)
        python.place(x=180, y=150)

        # Radiobutton name Python
        java = Radiobutton(self.subroot, text="Java", command=self.Que, font="calibri 20 bold", variable=self.var, value=2)
        java.place(x=310, y=150)

        # Radiobutton name Python
        csharp = Radiobutton(self.subroot, text="C Sharp", command=self.Que, font="calibri 20 bold", variable=self.var, value=3)
        csharp.place(x=420, y=150)

        self.subroot.geometry("800x450")
        self.subroot.mainloop()

