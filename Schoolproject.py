import time
import hmtai
import os
import webbrowser as wb

def StartUpMessage():
    print("##############################")
    print("# Schoolproject 1.1          #")
    print("# by BinStudent              #")
    print("##############################")

def Questions():
    print("1 = Neko | 2 = Yuri | 3 = Erotic | 4 = Vanilla | 5 = Ahegao | 6 = Uniform | 7 = Anal | 8 = Boobs | 9 = Pussy | 10 = Thighs\n11 = BDSM | 12 = Manga | 13 = Zettai Ryouiki | 14 = Glasses | 15 = Underwear | 16 = Masturbation | 17 = Public | 18 = Incest | 19 = Domination | 20 = Ass \n21 = Elves | 22 = Tentacles | 23 = Gif")

    category_ask = int(input("\nWich Category do you want?\n"))
    if category_ask == 1:
        category = "NSFWNeko"
    elif category_ask == 2:
        category == "yuri"
    elif category_ask == 3:
        category = "ero"
    elif category_ask == 4:
        category = "hentai"
    elif category_ask == 5:
        category = "ahegao"
    elif category_ask == 6:
        category = "uniform"
    elif category_ask == 7:
        category = "anal"
    elif category_ask == 8:
        category = "boobs"
    elif category_ask == 9:
        category = "pussy"
    elif category_ask == 10:
        category = "thighs"
    elif category_ask == 11:
        category = "bdsm"
    elif category_ask == 12:
        category = "manga"
    elif category_ask == 13:
        category = "zettaiRyouiki"
    elif category_ask == 14:
        category = "glasses"
    elif category_ask == 15:
        category = "pantsu"
    elif category_ask == 16:
        category = "masturbation"
    elif category_ask == 17:
        category = "public"
    elif category_ask == 18:
        category = "incest"
    elif category_ask == 19:
        category = "femdom"
    elif category_ask == 20:
        category = "ass"
    elif category_ask == 21:
        category = "elves"
    elif category_ask == 22:
        category = "tentacles"
    elif category_ask == 23:
        category = "gif"

    else:
        print("\nThis is not a Number or available!")
        time.sleep(3)
        os.system('cls')
        StartUpMessage()
        Questions()

    number_asked = int(input("\nHow much do you want to get?\n"))
    if number_asked < 31:
        for _ in range(number_asked):
            wb.open(hmtai.get("hmtai",category))
    else:
        print("\nThis is not Number or over 30!")
        time.sleep(3)
    os.system('cls')
    StartUpMessage()
    Questions()

StartUpMessage()
Questions()
