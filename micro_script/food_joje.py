resid=[]

def food_joje(num_joje:int,mablagh:int)->list:
    """قسمت سفارش و صورت حساب جوجه

    Args:
        num_kabab (int): تعداد جوجه
        mablagh (int): قیمت جوجه

    Returns:
        list: صورت حساب
    """
    price_tax_joje=1.1*num_joje*mablagh
    resid.append(price_tax_joje)
    print(resid)
    return resid