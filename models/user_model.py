def updateproducts(data1) -> dict:
    return {
        "id": str(data1['_id']),
        "product_name": data1['product_name'],
        "pcount" : data1['pcount'],
        "description" :data1['description'],
        "price": data1['price']
    }

def getallproducts(datas) -> list:
    return [updateproducts(data1) for data1 in datas]


def search_id(datas,id) ->str:
    ct=0
    for data in datas:
        if(data['_id']==id):
            ct+=1
            break
    if(ct==1):
        return "Yes"
    else:
        return "No"

def search_product(datas,id,product_name) -> str:
    ct=0
    for data in datas:
        if(data['id']==id and data['product_name']==product_name):
            ct+=1
            break
    if ct==0:
        return "No"
    else:
        return "Yes"

def find_one(datas,id) ->str:
    ct=0
    for data in datas:
        if(data['unique_id']==id and data['role']=='vendor'):
            ct+=1 
            break
    if(ct==0):
        return "No"
    else:
        return "Yes"
        

def statusdatas(datas) -> list:
    return [statusdata(data3) for data3 in datas]

def statusdata(data3) -> dict:
    return{
        "id":str(data3['_id']),
        "name": data3['name'],
        "status": data3['status']
    }

def get_products(datas) -> list:
    res=[]
    for data in datas:
        res.append(data['product_name'])
    return res









