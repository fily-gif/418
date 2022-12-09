# setting up stuff
import time
import colorama
init()
menuchoice = choice("[1] launch game, [2] credits, [3] exit")


def menu():
    print('Hello! and welcome to ' + Fore.RED + 'game name here')
    time.sleep(.4)
    print('what do you want to do?')
    print(menuchoice)