from tkinter import *
import Database
import pymongo

theDatabaseConnection ='mongodb://localhost:27017/'
theDatabase="Quiz_Application"

def searchQuery(Collection_Name,Query,myDB,WhereClause):
    if Collection_Name in myDB.list_collection_names():
        print("Collection Found")
        Collection= myDB[Collection_Name]
        for x in Collection.find(WhereClause,Query):
            print(x)
    else:
        print("not found")
def show_data(Collection_Name,myDB):
    Collection = myDB[Collection_Name]
    # Collection.aggregate({$sample:{size:1}})
    data = Collection.find({},{"_id":0,"Question":1,"Option1":1,"Option2":1,"Option3":1,"Option4":1}).limit(1)
    # for y in data:
    #     for x in y:
    #         print("\n",x,":",y[x])
    return data
try:
    myNoSQLDBCliebt = pymongo.MongoClient(theDatabaseConnection)
    # print("Connected")
    collection_name="Python_Quiz"
    myDB = myNoSQLDBCliebt[theDatabase]
        # col=myDB(collection_name)

except:
        print("ERROR")
class Question:
    def __init__(self):
        # root.destroy()
        self.gui = Tk()
        self.questionPage()

    def data(self):
        self.d= Database.show_data()

    def questionPage(self):
        var = IntVar()
        l1 = []
        self.gui.title("Quiz Application")
        dat=show_data(collection_name, myDB)
        # print(dat)
        for i in dat:
            print(i)

            for y in i.values():
                ques=y
                l1.append(ques)
                # print(l1)
                # print(i)
                # print(y)
        q_no = Label(self.gui, text=l1[0], width=60, #question number
        font=('ariel', 16, 'bold',), anchor='w', )
         # placing the option on the screen
        q_no.place(x=70, y=90)

        a = Radiobutton(self.gui, text= l1[1] ,font="calibri 12 bold", variable=var, value = 1)#value=hardQ&#91;x]&#91;1],variable = var,
        a.place(x=70, y=150, anchor='w')

        b = Radiobutton(self.gui,  text=l1[2],font="calibri 12 bold", variable=var, value = 2) # &  # 91;x]&#91;2] value=hardQ&#91;x]&#91;2],variable = var,
        b.place(x=70, y=200, anchor='w')

        c = Radiobutton(self.gui, text=l1[3] ,font="calibri 12 bold", variable=var, value = 3) # &  # 91;x]&#91;3] ,value=hardQ&#91;x]&#91;3],variable = varvalue=hardQ&#91;x]&#91;4],variable = var,
        c.place(x=70, y=250, anchor='w')

        d = Radiobutton(self.gui, text=l1[4] ,font="calibri 12 bold", value = 4, variable=var) #&  # 91;x]&#91;4]
        d.place(x=70, y=300, anchor='w')


        self.gui.geometry("800x450")
        self.gui.mainloop()

if __name__ == '__main__':
    q1=Question()


