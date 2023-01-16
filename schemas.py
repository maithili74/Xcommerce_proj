from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str
    role :str
    email: str
    phone : str

class login(BaseModel):
    phone :str
    password :str


class data(BaseModel):
    name :str
    status :str

class add_product(BaseModel):
    name : str
    product_id : str
    unique_id :str
    description :str
    pricing :str


