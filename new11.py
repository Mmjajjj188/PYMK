import random
import requests
import time

from colorama import *

req = requests.session()
print(f"""{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}===================================

""")
# noinspection PyUnboundLocalVariable
time.sleep(8)
print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Checker By 5m4d")
time.sleep(6)
print(f"""{Style.BRIGHT}{Fore.LIGHTGREEN_EX}
insta: @v.tdl
{Fore.LIGHTCYAN_EX}tele: @ZZZNZN
{Fore.LIGHTRED_EX}Good Luck""")
time.sleep(4)
print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}===================================")
time.sleep(3 / 150)

b = 0
a = 0
char = 'abcdefghijklmnopqrstuvwxyz01234567890_.'
rof = int(input("""[+] Users Length : 
--> """))
sleep = int(input('Sleep Time: '))
TOK = input('Token Bot: ')
ID = input('Tele ID: ')
print(""
      )
print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}===================================")
print(""
      )
print(f"""{Fore.LIGHTRED_EX}{Style.BRIGHT}Check Started By @ZZZNZN
{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Good Luck""")
print(""
      )
print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}===================================")
print(""
      )
while True:
    pass

    checklist = str("".join(random.choice(char) for i in range(rof)))
    tikurl = f"https://www.tiktok.com/@{checklist}?"
    headersop = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }

    sendcheckerwithoutsession = req.get(tikurl, headers=headersop)
    if sendcheckerwithoutsession.status_code == 404:
        a += 1
        print(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{[a]} Good New User: {checklist}')
        print(""
              )
        with open("Hunted Users By @ZZSNN.txt", "a") as Hunted:
            Hunted.write(checklist + "\n")
            Bot = f'https://api.telegram.org/bot{TOK}/sendMessage?chat_id={ID}&text= TikTok Hunted: {checklist}\nBy : @ZZSNN'
            req.get(Bot)

    else:
        b += 1
        print(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}{[b]} NoPe: {checklist}')
        print(""
              )
        time.sleep(sleep)
