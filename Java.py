import pymongo
import Data as D
theDatabaseConnection = 'mongodb://localhost:27017/'
theDatabase = 'java'
try:
    myClient = pymongo.MongoClient(theDatabaseConnection)  # connecting to database
    print("Connected successfully")
    mydb = myClient[theDatabase]  # Database creation
    print("Database Created")
    javaQuiz = mydb['JavaQuiz']  # collection creation name JavaQuiz
    if 'JavaQuiz' in mydb.list_collection_names():
        print("Collection Found")
    else:
        print("Collection not found")

    def insert_data(collectionName, query):
        try:
            collectionName.insert_one(query)
            print("Data inserted successfully")
        except:
            print("insertion failed")


    for x in D.easyQue:
        insert_data(javaQuiz, x)

    for x in D.mediumQue:
        insert_data(javaQuiz, x)

    for x in D.hardQue:
        insert_data(javaQuiz, x)


except:
    print("connection failed")
finally:
    myClient.close()
    print("connection closed")

