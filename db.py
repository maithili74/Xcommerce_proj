import pymongo
from enum1 import Status
from dotenv import load_dotenv
import os 

load_dotenv()
link=os.getenv("mongodb")
client=pymongo.MongoClient(link)
db =client['Job_search']
job=db['total_jobs']
apply_products=db['Products_List']
login=db['registration_details']
#status=db['status_details']



def create_job(data):
    data=dict(data)
    job.insert_one(data)

def products(data):
    data=dict(data)
    