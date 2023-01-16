from fastapi import APIRouter,Depends,HTTPException
import db
import models.user_model as user_model 
from schemas import add_product
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg,error,admin

vendor_route =APIRouter(
    prefix='/vendor',
    tags=['vendor']
)


@vendor_route.post("/add_product")
async def add_product(id, products : add_product,username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    a= user_model.find_one(db.vendor.find(),id)
    if(b=="Yes"):
        if(a=="Yes"):
            db.products.insert_one(dict(products))
            return "sucessfully product uploaded"
        else:
            raise HTTPException(status_code=401, detail=admin['message'].value )
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )

@vendor_route.get("/product_list")
async def product_list(id, username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    if(b=="Yes"):
        a = user_model.product_list(db.products.find(),id)
        return a
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )

@vendor_route.get("/search")
async def search(id,name,username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    if(b=="Yes"):
        a = user_model.search_product(db.products.find(),id,name)
        return a
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )

