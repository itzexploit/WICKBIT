from requests import get
from bs4 import BeautifulSoup
from colorama import Fore , init
from os import system , name
from pystyle import Colorate , Colors

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = '''

        ---      --- --------  ------------ ----    ---- -----------  --------  ------------ 
        ***  **  *** ********  ************ ****   ****  ***********  ********  ************ 
        ---  --  ---   ----    ---          ----  ----   ----       -   ----    ------------ 
        ***  **  ***   ****    ***          *********    ***********    ****        ****     
        ---  --  ---   ----    ---          ---------    -----------    ----        ----     
        ************   ****    ***          ****  ****   ****       *   ****        ****     
         ----------  --------  ------------ ----   ----  -----------  --------      ----     
          ********   ********  ************ ****    **** ***********  ********      ****     
                                                                                     
                                *** Created By John Wick ***

'''

print(Colorate.Horizontal(Colors.red_to_blue,banner,1))

api_b = 'https://coinmarketcap.com/currencies/bitcoin/'
api_et = 'https://coinmarketcap.com/currencies/ethereum/'
api_bn = 'https://coinmarketcap.com/currencies/bnb/'
api_s = 'https://coinmarketcap.com/currencies/solana/'
api_us = 'https://coinmarketcap.com/currencies/usd-coin/'
api_x = 'https://coinmarketcap.com/currencies/xrp/'
api_to = 'https://coinmarketcap.com/currencies/toncoin/'

def bit():
    try:
        r = get(api_b).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}\n    [{green}${white}] {blue}Bitcoin {red}:{green} ',pr)
    except:
        pass

def et():
    try:
        r = get(api_et).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}    [{green}${white}] {blue}Ethereum {red}:{green} ',pr)
    except:
        pass

def bn():
    try:
        r = get(api_bn).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}    [{green}${white}] {blue}Bnb {red}:{green} ',pr)
    except:
        pass

def s():
    try:
        r = get(api_s).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}    [{green}${white}] {blue}Solena {red}:{green} ',pr)
    except:
        pass

def us():
    try:
        r = get(api_us).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}    [{green}${white}] {blue}Usd-Coin {red}:{green} ',pr)
    except:
        pass

def x():
    try:
        r = get(api_x).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}    [{green}${white}] {blue}Xrp {red}:{green} ',pr)
    except:
        pass

def to():
    try:
        r = get(api_to).content
        soup = BeautifulSoup(r , features='html.parser')
        pr = soup.find('span',attrs={'class':'sc-f70bb44c-0 jxpCgO base-text'}).text
        print(f'{white}    [{green}${white}] {blue}Toncoin {red}:{green} ',pr)
    except:
        pass

bit()
et()
bn()
s()
us()
x()
to()
