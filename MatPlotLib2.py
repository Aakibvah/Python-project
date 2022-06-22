import Database
import matplotlib.pyplot as plt
import numpy as np
import Questions
import loginPage

class Matplotlib_2:
    def __init__(self):
        self.j_count = 0
        self.p_count = 0
        self.c_count = 0
        self.dict = {}
        self.counterList = []
        self.subject_List = []

    def connect(self):
        self.dict = Database.show_data1(loginPage.login.email,Database.myDB)
        for x in self.dict:
            if x['Subject'] == "Csharp":
                self.c_count += 1
            elif x['Subject'] == "Java":
                self.j_count += 1
            elif x['Subject'] == "Python":
                self.p_count += 1


        self.counterList.append(self.c_count)
        self.counterList.append(self.j_count)
        self.counterList.append(self.p_count)

        self.subject_List.append("Csharp")
        self.subject_List.append("Java")
        self.subject_List.append("Python")

        x = np.array(self.subject_List)
        y = np.array(self.counterList)

        plt.bar(x, y, color="blue", width=.5)
        plt.title("Total number of attempts in particular subject")
        plt.xlabel("Subject")
        plt.ylabel("Attempt")
        plt.show()

