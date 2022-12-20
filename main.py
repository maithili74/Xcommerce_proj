from fastapi import FastAPI,Depends
from routers.auth_router import auth_route
from routers.product_router import product_route
from routers.vendor_router import vendor_route
#from controllers.auth_controller import auth_handler

app=FastAPI(
    title='E-Commerce',
    description='This is an Online Shopping website',
)

app.include_router(auth_route)
app.include_router(product_route)
app.include_router(vendor_route)

#@app.get('/')
#def index(username=Depends(auth_handler.auth_wrapper)):
    #return "sucess"


