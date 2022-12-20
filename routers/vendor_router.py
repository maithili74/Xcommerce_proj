from fastapi import APIRouter,File,UploadFile,Depends,HTTPException
import db
import models.user_model as user_model 
from schemas import products
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg
from controllers.vendor_controller import vendor_controller

vendor_route =APIRouter(
    prefix='/vendor',
    tags=['Vendor']
)


@vendor_route.post("/add_product")
async def apply_products(data : products,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='vendor':
        # candidate_controller.applyjob(dict(data))
        db.apply_products.insert_one(dict(data))
        return " sucessfully added"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@vendor_route.get('/product_list')
async def get_applied_products(username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='vendor':
        # candidate_controller.get_applied_jobs
        b=user_model.totaljobs(db.apply_products.find())
        return b
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@vendor_route.get("/search")
async def singlecandidate(id,product_name, username=Depends(auth_handler.auth_wrapper)):
    b=user_model.search_id(db.login.find(),id)
    if(b=="Yes"):
        a=user_model.search_product(db.apply_products.find(),id,product_name)
        return a
    else:
        return "Id doesnt exist"
      

    


