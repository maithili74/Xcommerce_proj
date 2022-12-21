import pymongo
from enum1 import Status
from dotenv import load_dotenv
import os 

load_dotenv()
link=os.getenv("mongodb")
client=pymongo.MongoClient(link)
db =client['E-Commerce']
#job=db['total_jobs']
apply_products=db['Products_List']
login=db['registration_details']

    