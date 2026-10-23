resid=[]

def tea(num_tea:int,mablagh:int)->list:
    """قسمت سفارش و صورت حساب چای

    Args:
        num_kabab (int): تعداد چای
        mablagh (int): قیمت چای

    Returns:
        list: صورت حساب
    """
    price_tax_tea=1.1*num_tea*mablagh
    resid.append(price_tax_tea)
    print(resid)
    return resid