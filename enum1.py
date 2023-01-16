from enum import Enum

class Status(Enum):
    under_process = "Under Process"

class role(Enum):
    vendor="vendor"
    Candidate ="candidate"
    Admin="admin"

class msg(Enum):
    message='You are not Allowed!!'

class error(Enum):
    message = "Id doesn,t exist!!"

class admin(Enum):
    message = "Admin doesn't have access!!!"

class vendor(Enum):
    message=" Vendor doesn't have access!!"

