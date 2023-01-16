def logindata(data2) -> dict:
    return {
        "_id": str(data2['_id']),
        "phone": data2['phone'],
        "password" : data2['password']
    }

def login(datas) -> list:
    return [logindata(data2) for data2 in datas]

def register(data2) -> dict:
    return {
        "_id": str(data2['_id']),
        "username": data2['username'],
        "role" :data2['role'],
        'email' :data2['email']
    }

def registerdatas(datas) -> list:
    return [register(data2) for data2 in datas]    