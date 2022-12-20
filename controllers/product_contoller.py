import db
import models.user_model as user_model

class product_controller():
    #def getalljobs():
        #a=user_model.totaljobs(db.login.find())
    
    def totalproducts():
        user_model.totaljobs(db.apply_products.find())
    
    def singleproduct(title):
        user_model.jobapplication(db.job.find_one({"title": title}))