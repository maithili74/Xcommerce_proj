from fastapi import APIRouter
from schemas import AuthDetails,login
from controllers.auth_controller import auth_controller,auth_role,unique_id

auth_route=APIRouter(
    prefix='/auth',
    tags=['auth']
)


@auth_route.post("/register")
async def register(auth_details : AuthDetails):
    auth_controller.auth_register(auth_details)
    return {
            "Username" : auth_details.username,
            "unique_id" : unique_id,
            "email" :auth_details.email,
            "role": auth_details.role,
            "status" : True,
            "Message" : "sucessfully Registered"
    }

@auth_route.post('/login')
def login(auth_details: login):
    auth_controller.auth_login(auth_details)
    return {
        "token" : auth_role.token,
        "user" : auth_role.data
    }

