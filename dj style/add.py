



data=[]

data_dict={}

def add_kala(p_id:int,esm:str,price:int,mojoodi:int)->list[dict]:
    data_dict[p_id]={"name kala":esm,"gheymat":price,"mojoodi":mojoodi}
    print(data_dict)
    
    print("-"*20)
    
    data.append(data_dict)
    
    print(data)
    
    print("*"*20)