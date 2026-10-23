resid=[]

def cappuccino(num_cappuccino:int,mablagh:int)->list:
    """قسمت سفارش و صورت حساب کاپوچینو

    Args:
        num_kabab (int): تعداد کاپوچینو
        mablagh (int): قیمت کاپوچینو

    Returns:
        list: صورت حساب
    """
    price_tax_cappuccino=1.1*num_cappuccino*mablagh
    resid.append(price_tax_cappuccino)
    print(resid)
    return resid