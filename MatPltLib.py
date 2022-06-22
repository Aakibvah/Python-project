import Database
import matplotlib.pyplot as plt
import numpy as np
import Questions
import loginPage
class Matplotlib:



    def __init__(self):
        self.dict = {}
        self.python_Time =[]
        self.python_Score =[]
        self.java_Time =[]
        self.java_Score =[]
        self.csharp_Time=[]
        self.csharp_Score =[]


    def progress(self):
        xpoints = []
        ypoints = []
        subject =Questions.Question.subject

        self.dict =Database.show_data1(loginPage.login.email,Database.myDB)
        for y in self.dict:
            if(y['Subject'] =='Python'):
                self.python_Time.append(y['Time'])
                self.python_Score.append(y['Score'])
            elif(y['Subject'] =='Java'):
                self.java_Time.append(y['Time'])
                self.java_Score.append(y['Score'])
            elif(y['Subject'] =='Csharp'):
                self.csharp_Time.append(y['Time'])
                self.csharp_Score.append(y['Score'])



        if(subject=="Java"):
            xpoints = np.array(self.java_Score)
            ypoints = np.array(self.java_Time)
            print("Your average score :-" ,np.mean(self.java_Score))
            plt.title("Java Scores")

        elif(subject=="Python"):
            xpoints = np.array(self.python_Score)
            ypoints = np.array(self.python_Time)
            print("Your average score :-",np.mean(self.python_Score))

            plt.title("Python Scores")

        elif (subject == "Csharp"):
            xpoints = np.array(self.csharp_Score)
            ypoints = np.array(self.csharp_Time)
            print("Your average score :-" ,np.mean(self.csharp_Score))

            plt.title("Csharp Scores")
        plt.scatter(xpoints, ypoints)
        plt.plot(xpoints, ypoints)
        plt.ylabel("Date")
        plt.xlabel("Scores")
        plt.show()
