



list_pass=["12345","123456"]

list_user=["admin","admin123"]

def user_pass(user:str,password:str):
    while True:
        if user.isspace()!=True and user.isascii()==True:
            if password.isalnum()==True and password.isspace()!=True:
                if user in list_user and password in list_pass:
                    return("login admin")
                
        else:
            continue