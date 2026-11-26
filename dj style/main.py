




from add import add_kala

from admin_panel import user_pass


def main():
    while True:
        vorod=input("1.admin 2.adi 3.exit:")
        match vorod:
            case "1":
                username=input("enter user:")
                password_vorodi=input("enter password:")
                user_pass(user=username,password=password_vorodi)
                
                if user_pass(user=username,password=password_vorodi) is "login admin":
                    id_kala=int(input("id kala:"))
                    add_kala(p_id=id_kala)
                    
main()