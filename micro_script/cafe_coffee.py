resid=[]

def coffee(num_coffee:int,mablagh:int)->list:
    """قسمت سفارش و صورت حساب قهوه

    Args:
        num_kabab (int): تعداد قهوه
        mablagh (int): قیمت قهوه

    Returns:
        list: صورت حساب
    """
    price_tax_coffee=1.1*num_coffee*mablagh
    resid.append(price_tax_coffee)
    print(resid)
    return resid