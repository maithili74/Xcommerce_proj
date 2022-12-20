import db 
import models.user_model as user_model

class vendor_controller():
    #def applyjob(data):
        #db.apply_job(data)
    
    def get_applied_products():
        user_model.getallproducts(db.apply_products.find())
    
    #def searchdata(data,product_name):
        #user_model.totalappliedjobs(db.apply_job.find({"name":product_name}))
    