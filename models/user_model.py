
def product_list(datas,id) -> list:
    res=[]
    for data in datas:
        if(data['unique_id']==id):
            res.append(data['name'])
    return res

def search_product(datas,id,name) -> str:
    ct=0
    for data in datas:
        if(data['unique_id']==id and data['name']==name):
            ct+=1
            break
    if(ct==0):
        return "No"
    else:
        return "Yes"
def search_id(datas,id) ->str:
    ct=0
    for data in datas:
        if(data['unique_id']==id):
            ct+=1 
            break
    if(ct==0):
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

def get_vendors(datas) -> list:
    res=[]
    for data in datas:
        del data['_id']
        res.append(data['username'])
    return res 

def get_all_products(datas) -> list:
    res=[]
    for data in datas:
        res.append(data['name'])
    return res

def statusdata(data3) -> dict:
    return {
        "id": str(data3['_id']),
        "name" : data3['name'],
        "status": data3['status']
        
    }

def statusdatas(datas) -> list:
    return [statusdata(data3) for data3 in datas]

