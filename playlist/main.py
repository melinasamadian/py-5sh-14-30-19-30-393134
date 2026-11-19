



from add_ahang import add_song
from delete import hazf_ahang


main_dict={}


while True:
    menu=input("1.add 2.show 3.delete 4.find 5.edit 6.exit:")
    while True:
        match menu:
            case "1":
                name_song=input("enter a song:")
                
                singer=input("enter singers name:")
                
                style=input("enter the song style:")
                
                album=input("album:")
                
                item_movaghat={name_song:{"singer":singer,"style":style,"album":album}}
                
                main_dict.update(item_movaghat)
                add_song(esm_ahang=name_song,khanande=singer,sabk=style,allbum=album)
                break
                
            case "2":
                pass
            case "3":
                esme_muzic=input("esm bede:")
                hazf_ahang(esm_ahang=esme_muzic)
                break