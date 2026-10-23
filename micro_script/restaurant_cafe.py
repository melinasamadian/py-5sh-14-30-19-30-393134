from food_kabab import *

from food_joje import *

from food_makarani import *

from cafe_coffee import *

from cafe_tea import *

from cafe_cappuccino import *

while True:
    menu=input("1.restaurant 2.cafe 3.exit:")

    while True:
        match menu:
            case "1":
                menu_food=input("1.kabab 2.joje 3.makarani 4.exit:")
                match menu_food:
                    case "1":
                        num_kabab=int(input("how many?"))
                        mablagh=int(input("mablagh?"))
                        food_kabab(num_kabab,mablagh)

                    case "2":
                        num_joje=int(input("how many?"))
                        mablagh=int(input("mablagh?"))
                        food_joje(num_joje,mablagh)

                    case "3":
                        num_makarani=int(input("how many?"))
                        mablagh=int(input("mablagh?"))
                        food_makarani(num_makarani,mablagh)

                    case "4":
                        break

            case "2":
                memu_cafe=input("1.coffee 2.tea 3.cappuccino 4.exit:")
                match memu_cafe:
                    case "1":
                        num_coffee=int(input("how many?"))
                        mablagh=int(input("mablagh?"))
                        
                        coffee(num_coffee,mablagh)
                        break
                    case "2":
                        num_tea=int(input("how many?"))
                        mablagh=int(input("mablagh?"))
                                                
                        tea(num_tea,mablagh)
                        break
                    case "3":
                        num_cappuccino=int(input("how many?"))
                        mablagh=int(input("mablagh?"))
                                                
                        cappuccino(num_cappuccino,mablagh)
                        break
                    case "4":
                        break