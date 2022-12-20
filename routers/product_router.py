from fastapi import APIRouter,Depends,HTTPException
import db
import models.user_model as user_model 
from schemas import creat_job,data
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg

product_route=APIRouter(
    prefix='/admin',
    tags=['Admin']
)

    

@product_route.get("/get_vendors")
async def get_vendor(username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='vendor':
        a=user_model.totalproducts(db.login.find())  
        return  a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@product_route.get('/product_list')
async def get_applied_products(username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='vendor':
        b=user_model.totalproducts(db.login.find())
        return b
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@product_route.get("/get_all_products")
async def singleproduct(title,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='admin':
        a =user_model.jobapplication(db.job.find_one({"title": title}))
        return a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@product_route.get("/search")
async def singleproduct(title,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='admin':
        a =user_model.jobapplication(db.job.find_one({"title": title}))
        return a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@product_route.put("/update/")
async def update(name, data1 :data,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='admin':
        db.status.find_one_and_update({"name": name}, {
        "$set": dict(data1)
        })
        return "status updated"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)
