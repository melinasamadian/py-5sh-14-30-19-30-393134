






from show_ahang import*

main_list_ahang=[]
def add_song(esm_ahang:str,khanande:str,sabk:str,allbum:str)->dict:
    
    global main_list_ahang
    main_list_ahang2={"nam ahang":esm_ahang,"nam khanande":khanande,"sabk ahang":sabk,"album":allbum}
    
    main_list_ahang.append(main_list_ahang2)
    
    print(main_list_ahang)
    
    
    