resid=[]

def food_makarani(num_makarani:int,mablagh:int)->list:
    """قسمت سفارش و صورت حساب ماکارانی

    Args:
        num_kabab (int): تعداد ماکارانی
        mablagh (int): قیمت ماکارانی

    Returns:
        list: صورت حساب
    """
    price_tax_makarani=1.1*num_makarani*mablagh
    resid.append(price_tax_makarani)
    print(resid)
    return resid