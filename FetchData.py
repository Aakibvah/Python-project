# import Database
#
# def rand_number():
#     import random
#     a = random.randint(1, 10)
#     return a
#
# Database.show_data("Python_Quiz",Database.myDB,1,rand_number())
# input = input("Please enter the Answer as Option1 , Option2 , Option3, Option4")
#
# WhereClause = {"Correct_answer": {"$regex": "^A"}}
# SearchQuery2 = {"_id": 0, "First_Name": 1, "Last_Name": 1, "Manager_Name": 1}
# # searchQuery(Employee_Collection_Name, SearchQuery2, myDB, WhereClause)
#
#
# Database.searchQuery("Python_Quiz",Database.myDB,{})