from treelib import Node, Tree
import treelib
from random import randint
import requests
import json
from colorama import Fore, init
from bs4 import BeautifulSoup
from treelib import Tree
import os
import pymysql
from datetime import date
import tkinter as tk
from tkinter import filedialog
init()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    title = f"NumGen" 
    os.system("title " + str(title))
    logo = f"""{Fore.BLUE}
     ▐ ▄ ▄• ▄▌• ▌ ▄ ·.  ▄▄ • ▄▄▄ . ▐ ▄ 
    •█▌▐██▪██▌·██ ▐███▪▐█ ▀ ▪▀▄.▀·•█▌▐█
    ▐█▐▐▌█▌▐█▌▐█ ▌▐▌▐█·▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
    ██▐█▌▐█▄█▌██ ██▌▐█▌▐█▄▪▐█▐█▄▄▌██▐█▌
    ▀▀ █▪ ▀▀▀ ▀▀  █▪▀▀▀·▀▀▀▀  ▀▀▀ ▀▀ █▪
    {Fore.YELLOW}
    """
    print(logo)
    key = input("[Key]: ")
    connection = pymysql.connect(
        user='toronto', 
        passwd='XXXXXXXXXXXX', 
        host='mysql-toronto.alwaysdata.net', 
        database='toronto_apache'
        )
    cursor = connection.cursor()
    query = ("SELECT * FROM keys_access WHERE key_access = (" + key + ")")
    cursor.execute(query)
    connect = [str(i) for i in cursor]
    if connect:
        while True:
            print(f"""
                {Fore.YELLOW}[{Fore.RED}GENERATE NUMLIST{Fore.YELLOW}]: 1 
                {Fore.YELLOW}[{Fore.RED}SCAN NUMLIST{Fore.YELLOW}]: 2""")
            numlen = input("[*]> ")

            if numlen == "1":
                today = date.today()
                number = input("[NUMBER] ")
                n = 8
                x = 0
                numbers = []
                while x < int(number): 
                    french = "06" + ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
                    numbers.append(french)
                    x += 1
                with open("x" + number + "-NUMS-" + str(today) + ".txt", "a+") as file:
                    for i in numbers:
                        file.write(i + "\n")
                print(f"{Fore.GREEN}OUTPUT: " + "x" + number + "-NUMS-" + str(today) + ".txt")
                continue

            if numlen == "2":
                today = date.today()
                path = "HITS-" + str(today)
                try:
                    os.mkdir(path)
                except FileExistsError:
                    pass

                tree = Tree()
                root = tk.Tk()
                root.withdraw()
                file = filedialog.askopenfilename()
                v = open(file, "r", encoding="utf8").readlines()
                nums = [str(i).strip() for i in v]
                try:
                    valid = 0
                    hit = 0
                    check = 0
                    for i in nums:
                        check += 1
                        title = f"NumGen - [NUMs]: {check}/{len(nums)} - [HITs]: {hit}" 
                        os.system("title " + str(title))
                        b = i[5:]
                        a = requests.get(f"https://www.arcep.fr/demarches-et-services/professionnels/base-numerotation.html?tx_arcepbasetechnique_basetechnique%5B__referrer%5D%5B%40extension%5D=ArcepBasetechnique&tx_arcepbasetechnique_basetechnique%5B__referrer%5D%5B%40vendor%5D=GAYA&tx_arcepbasetechnique_basetechnique%5B__referrer%5D%5B%40controller%5D=BaseTechnique&tx_arcepbasetechnique_basetechnique%5B__referrer%5D%5B%40action%5D=search&tx_arcepbasetechnique_basetechnique%5B__referrer%5D%5Barguments%5D=YTowOnt93f79ac872f3e891e3d121304494af15ceeb744e4&tx_arcepbasetechnique_basetechnique%5B__referrer%5D%5B%40request%5D=a%3A4%3A%7Bs%3A10%3A%22%40extension%22%3Bs%3A18%3A%22ArcepBasetechnique%22%3Bs%3A11%3A%22%40controller%22%3Bs%3A13%3A%22BaseTechnique%22%3Bs%3A7%3A%22%40action%22%3Bs%3A6%3A%22search%22%3Bs%3A7%3A%22%40vendor%22%3Bs%3A4%3A%22GAYA%22%3B%7Da2bf59f355c30621a92ab741b949e14e74a32abc&tx_arcepbasetechnique_basetechnique%5B__trustedProperties%5D=a%3A1%3A%7Bs%3A6%3A%22search%22%3Ba%3A1%3A%7Bs%3A7%3A%22numeros%22%3Bi%3A1%3B%7D%7D6c5a73b9b235b8db1e19b0bafed7ac83147025d4&tx_arcepbasetechnique_basetechnique%5Bsearch%5D%5Bnumeros%5D={b}#c981")
                        valid = a.text
                        soup = BeautifulSoup(a.content, 'html.parser')
                        table = soup.find_all('span', attrs={"class":"red"})
                        if "a été attribué à" in valid:
                            hit += 1
                            v = str(table[1]).split('<span class="red">')[1].split("<")[0]
                            if "e*Message Wireless Information Services France" in v:
                                pass
                            else:
                                tree = Tree()
                                tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}Numéro{Fore.YELLOW}]:{Fore.YELLOW} {i}", "num")
                                tree.create_node(f"{Fore.YELLOW}[{Fore.GREEN}Opérateur{Fore.YELLOW}]{Fore.YELLOW}: {v}", "operateur", parent="num")
                                tree.show()
                                with open("NUMS-HITS-" + str(today) + ".txt", "a+") as numsfile:
                                    numsfile.write(i + "\n")
                                with open("HITS-" + str(today) + "/" + v + ".txt", "a+") as operator:
                                    operator.write(i + "\n")
                        else:
                            tree = Tree()
                            tree.create_node(f"{Fore.YELLOW}[{Fore.RED}Numéro{Fore.YELLOW}]:{Fore.YELLOW} {i}", "num")
                            tree.create_node(f"{Fore.YELLOW}[{Fore.RED}Invalide{Fore.YELLOW}]", "operateur", parent="num")
                            tree.show()
                except OSError:
                    pass
            else:
                print(f"{Fore.RED}[Exit]{Fore.RESET}")

main()
