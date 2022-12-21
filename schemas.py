from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str
    role :str
    fullname :str
    phone : str
    email : str

class login(BaseModel):
    email :str
    password :str


class products(BaseModel):
    product_name : str
    pcount:str
    description :str
    price:str

class data(BaseModel):
    name :str
    pcount : str
    description : str
    price : str

