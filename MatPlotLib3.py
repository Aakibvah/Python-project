import Database
import matplotlib.pyplot as plt
import numpy as np
import Questions
import loginPage

class Matplotlib_3:
    def __init__(self):
        self.j_max = []
        self.p_max = []
        self.c_max = []
        self.dict = {}
        self.subject_List = []
        self.max = []

    def connect(self):
        self.dict = Database.show_data1(loginPage.login.email,Database.myDB)
        # print("asdf",self.dict)
        for x in self.dict:
            if x['Subject'] == "Csharp" :
                self.c_max.append(x['Score'])
            elif x['Subject'] == "Java":
                self.j_max.append(x['Score'])
            elif x['Subject'] == "Python":
                self.p_max.append(x['Score'])


        # self.java_Max = self.j_max.sort()[0]
        # self.python_Max = self.p_max.sort()[0]
        self.p_max.sort(reverse = True)
        self.j_max.sort(reverse=True)
        self.c_max.sort(reverse=True)

        # self.csharp_Max = self.c_max.sort()[0]

        self.subject_List.append("Csharp")
        self.subject_List.append("Java")
        self.subject_List.append("Python")

        self.max.append(self.c_max[0])
        self.max.append(self.j_max[0])
        self.max.append(self.p_max[0])

        x = np.array(self.subject_List)
        y = np.array(self.max)

        plt.bar(x, y, color="blue", width=.5)
        plt.title("Highest Score  in particular subject")
        plt.xlabel("Subject")
        plt.ylabel("Score")
        plt.show()

