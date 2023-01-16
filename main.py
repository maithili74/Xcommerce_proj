from fastapi import FastAPI
from routers.auth_router import auth_route
from routers.admin_router import admin_route
from routers.vendor_router import vendor_route
app=FastAPI(
    title='Xcommerce',
    description='Vendor Admin Manager',
)

app.include_router(auth_route)
app.include_router(vendor_route)
app.include_router(admin_route)

