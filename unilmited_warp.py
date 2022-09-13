import json
import datetime
import time , requests , random , string
import urllib
from pyfiglet import Figlet
from rainbowtext import text
from colorama import Fore
def rand_number():
    return str(random.randint(1,999))

def rand_string(number):
    text = string.ascii_letters + string.digits
    result= ''.join(random.choice(text) for ch in range(number))
    return result


session = requests.Session()
url = "https://api.cloudflareclient.com/v0a%s/reg" % rand_number()



def warp_unlimited(id_code):
    inst = rand_string(22)
    body = {"key": "{}=".format(rand_string(43)),
        "install_id": inst,
        "fcm_token": "{}:APA91b{}".format(inst, rand_string(134)),
        "referrer": id_code,
        "warp_enabled": False,
        "locale": "es_US"}
    data = json.dumps(body).encode('utf8')
    header = {'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'okhttp/3.12.1'
        }
    try:
        req = urllib.request.Request(url , data , header)
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        time.sleep(5)
        continue

        
banner = Figlet(font="whimsy").renderText("Warp Fox")

print (text(banner))
print (Fore.RED + "[$] Created By Maximum Radikali")
print (Fore.GREEN + "[$] Channel ~> @BlackFoxSecurityTeam")
print (Fore.LIGHTMAGENTA_EX + "[&] Warp Plus Unlimited Script ! ")
print (Fore.YELLOW + "=====================================") ; code_id = input(Fore.CYAN + "[+] Please Enter Your Client ID : ")


while True:
    try:
        warp_unlimited(code_id)

        print ( Fore.GREEN + "Success ! You Got 1GB Warp + \n" + Fore.MAGENTA + "Please Wait 17 Second !")
        
        time.sleep(17)
    except KeyboardInterrupt:
        print (Fore.Red + "Stopped ! ")
