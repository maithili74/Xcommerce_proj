from fastapi import APIRouter,Depends,HTTPException
import db
import models.user_model as user_model 
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg,vendor,error

admin_route=APIRouter(
    prefix='/admin',
    tags=['Admin']
)



@admin_route.get("/get_vendors")
async def get_vendors(id,username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    a = user_model.find_one(db.vendor.find(), id)
    if(b=="Yes"):
        if(a=="No"):
            x = user_model.get_vendors(db.vendor.find())
            return x
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )


'''@admin_route.get("/product_list/")
async def product_list(id, username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    a = user_model.find_one(db.vendor.find(), id)
    if(b=="Yes"):
        if(a=="No"):
            x = user_model.product_list(db.products.find(),id)
            return x
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )'''

@admin_route.get("/get_all_products")
async def get_all_products(id,username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    a = user_model.find_one(db.vendor.find(), id)
    if(b=="Yes"):
        if(a=="No"):
            x= user_model.get_all_products(db.products.find())
            return x
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )

@admin_route.get("/search/")
async def search(id,name,username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    a = user_model.find_one(db.vendor.find(), id)
    if(b=="Yes"):
        if(a=="Yes"):
            b = user_model.search_product(db.products.find(),id,name)
            return b
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )


'''@admin_route.delete("/delete_vendor")
async def delete_vendor(id,username=Depends(auth_handler.auth_wrapper)):
    b = user_model.search_id(db.vendor.find(), id)
    a = user_model.find_one(db.vendor.find(), id)
    if(b=="Yes"):
        if(a=="No"):
            x=db.vendor.delete_many({'id':id})
            if(x.deleted_count==0):
                return "User doesn't exist"
            else:
                return "User deleted successfully"
        else:
            raise HTTPException(status_code=401, detail=vendor['message'].value )
    else:
        raise HTTPException(status_code=401, detail=error['message'].value )'''