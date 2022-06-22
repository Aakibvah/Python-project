import Database
import numpy as np
import loginPage
import Questions
class Median:
    def __init__(self):
        self.dict = {}
        self.score = []
        self.methode()
    def methode(self):
        self.dict = Database.show_data1(loginPage.login.email,Database.myDB)
        for i in self.dict:
            if i["Subject"] == Questions.Question.subject:
                self.score.append(i["Score"])

        print(f"Median of {Questions.Question.subject} is {np.median(self.score)}")

