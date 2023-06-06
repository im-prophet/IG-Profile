import os
from colorama import Fore
os.system("pip install instaloader")
os.system("title Prophet's IG ""Version 1.2")
os.system("cls")
def menu():
    print(f"[{Fore.LIGHTBLUE_EX}Notice{Fore.WHITE}] Prophet's instagram loader Version 1.2 ")
    print(f"[{Fore.LIGHTBLUE_EX}Notice{Fore.WHITE}] Enter target's Instagram username")
    user = input(f"[{Fore.LIGHTBLUE_EX}>{Fore.WHITE}] ")
    os.system(f"instaloader --highlights {user}")
menu()