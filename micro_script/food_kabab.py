resid=[]

def food_kabab(num_kabab:int,mablagh:int)->list:
    """قسمت سفارش و صورت حساب کباب

    Args:
        num_kabab (int): تعداد کباب
        mablagh (int): قیمت کباب

    Returns:
        list: صورت حساب
    """
    price_tax_kabab=1.1*num_kabab*mablagh
    resid.append(price_tax_kabab)
    print(resid)
    return resid