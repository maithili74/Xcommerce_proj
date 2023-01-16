import pymongo
from enum1 import Status
from dotenv import load_dotenv
import os 

load_dotenv()
link=os.getenv("mongodb")
client=pymongo.MongoClient(link)
db =client['Ecommerce']
vendor=db['vendors']
products=db['products']

    

