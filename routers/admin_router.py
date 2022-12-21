from fastapi import APIRouter,Depends,HTTPException
import db
import models.user_model as user_model 
from schemas import creat_job,data
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg,vendor,error

product_route=APIRouter(
    prefix='/admin',
    tags=['Admin']
)

    

@product_route.get("/get_vendors")
async def get_vendor(id,username=Depends(auth_handler.auth_wrapper)):
    a = user_model.search_id(db.vendor.find(), id)
    b = user_model.find_one(db.vendor.find(), id)
    if(a=="Yes"):
        if(b=="No"):
            x = user_model.get_vendors(db.vendor.find())
            return x
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@product_route.get('/product_list')
async def get_applied_products(id,username=Depends(auth_handler.auth_wrapper)):
    a = user_model.search_id(db.vendor.find(), id)
    b = user_model.find_one(db.vendor.find(), id)
    if(a=="Yes"):
        if(b=="No"):
            x = user_model.product_list(db.products.find(),id)
            return x
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@product_route.get("/get_all_products")
async def singleproduct(id,product_name,username=Depends(auth_handler.auth_wrapper)):
    a = user_model.search_id(db.vendor.find(), id)
    b = user_model.find_one(db.vendor.find(), id)
    if(a=="Yes"):
        if(b=="No"):
            x= user_model.get_all_products(db.products.find())
            return x
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@product_route.get("/search")
async def singleproduct(title,username=Depends(auth_handler.auth_wrapper)):
    a = user_model.search_id(db.vendor.find(), id)
    b = user_model.find_one(db.vendor.find(), id)
    if(a=="Yes"):
        if(b=="No"):
            b = user_model.search_product(db.products.find(),id,name)
            return b
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


'''@product_route.put("/update/")
async def update(name, data1 :data,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='admin':
        db.status.find_one_and_update({"name": name}, {
        "$set": dict(data1)
        })
        return "status updated"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)'''
