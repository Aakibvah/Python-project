import pymongo
import math

theDatabaseConnection ='mongodb://localhost:27017/'
theDatabase="Quiz_Application"

# Generic function for insertion
def insert_my(collectionname,documnet):
    myDB[collectionname].insert_one(documnet)


def search_data(collectionname,condition):
    count=0
    for i in myDB[collectionname].find(condition):
        count+=1
    return count


def searchQuery(Collection_Name,Query,myDB,WhereClause):
    if Collection_Name in myDB.list_collection_names():
        print("Collection Found")
        Collection= myDB[Collection_Name]
        for x in Collection.find(WhereClause,Query):
            print(x)
    else:
        print("not found")

def updateQuery(Collection_Name,OldValues,myDB,NewValues):
    if Collection_Name in myDB.list_collection_names():
        print("Collection Found")
        Collection= myDB[Collection_Name]
        Collection.update_one(OldValues,{"$set":NewValues})
        for x in Collection.find():
            print(x)
    else:
        print("not found")

def createCollection(Collection_Name,Query,myDb):
    if Collection_Name in myDB.list_collection_names():
        # print("User alredy exist please login")
        return True

    else:
        Collection = myDB[Collection_Name]
        Collection.insert_one(Query)
        for x in Collection.find():
            print(x)

def deleteQuery(Collection_Name,Query,myDB):
    if Collection_Name in myDB.list_collection_names():
        print("Collection Found")
        Collection= myDB[Collection_Name]
        Collection.delete_one(Query)
        for x in Collection.find():
            print(x)
    else:
        print("not found")

def dropQuery(Collection_Name,myDB):
    Collection = myDB[Collection_Name]
    Collection.drop()
    if Collection_Name in myDB.list_collection_names():
        print("Collection not deleted successfully")
    else:
        print("Collection deleted successfully")

def show_data1(collection_name,myDB):
    return myDB[collection_name].find()


def show_data(Collection_Name,myDB,no):
    Collection = myDB[Collection_Name]
    data = Collection.find({},{"Question":1,"Option1":1,"Option2":1,"Option3":1,"Option4":1, "Correct_Answer":1}).limit(1).skip(no)
    return data





try:
    myNoSQLDBCliebt = pymongo.MongoClient(theDatabaseConnection)
    # print("Connected")
    myDB = myNoSQLDBCliebt[theDatabase]

except:
    print("Exception connecting to database")




