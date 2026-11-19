



from add_ahang import *
import show_ahang


def hazf_ahang(esm_ahang:str)->dict:
    
    
    global main_list_ahang
    print(main_list_ahang)
    my_song=tuple(main_list_ahang)
    my_song_list=list(my_song)
    print(my_song_list)
    for i in my_song_list:
        if i==esm_ahang:
            print(i,esm_ahang)
            q1=input("hazf ya na?(y/n):")
            match q1:
                case"1":
                    my_song_list.remove(esm_ahang)
                    print(my_song_list)
                case"2":
                    print("ok honney")
            
                