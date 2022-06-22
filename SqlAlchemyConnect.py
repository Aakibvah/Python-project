import sqlalchemy
from sqlalchemy import create_engine

try:
    engine = create_engine("mongodb:///?Server=MyServer&;Port=27017&Database=java&User=test&Password=Password")
    connection = engine.connect()
    print("connected successfilly")
except:
    print("Connection failed")