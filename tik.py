import requests
import random
import time
import json
import string
import os
import sys
import re
from threading import Thread, Lock
from user_agent import generate_user_agent as ua

# Colors
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = "\033[1;30m"
X = '\033[1;33m'
F = '\033[2;32m'
Z3 = '\033[1;31m'
L = "\033[1;95m"
C = '\033[2;35m'
A = '\033[2;39m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'

# Threading Safety
lock = Lock()
tiktok_good = 0
tiktok_bad = 0
email_good = 0
email_bad = 0

def elia5():
    sd = random.choice([J1, J2, J21, J22, F1, C1, P1, P2])
    os.system('clear||cls')
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22} [𝑬𝑳𝑰𝑨] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(sd + f"""

         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝

        {X}¸.•´¯`•.¸¸ {F} [꧁ 𝑬𝑳𝑰𝑨 - 𝑻𝑰𝑲𝑻𝑶𝑲 ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}TLE : @ELIA_py / @XRRHX
    """)
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22} [𝑬𝑳𝑰𝑨] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

elia5()
tok = input(' TOKEN : ')
iid = input(' ID : ')

def elia_innnn():
    with lock:
        sys.stdout.write(f"\r{X}TikTok Checked: {tiktok_good + tiktok_bad} • {F}Good: {tiktok_good} • {Z}Bad: {tiktok_bad} • {C1}Email Hit: {email_good} • {J2}Fail: {email_bad} ")
        sys.stdout.flush()

def elia88(username, followers):
    tlg = f'''
𝐓𝐈𝐊𝐓𝐎𝐊 𝐇𝐈𝐓 ✅
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
-𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
-𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
-𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers}
-𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗛𝗶𝘁 ✅
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
    '''
    try:
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", json={
            "chat_id": iid,
            "text": tlg,
            "reply_markup": {
                "inline_keyboard": [
                    [{"text": "ELIA", "url": "https://t.me/ELIA_Py"},
                     {"text": "Channel ", "url": "https://t.me/XRRHX"}]
                ]
            }
        })
    except:
        pass

def gmail_elia(email):
    """
    منطق Gmail الكامل (batchexecute) من g1.py
    """
    global email_bad, email_good
    try:
        username = email.split('@')[0]
        name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
        birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
        s = requests.Session()
        headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language':'en-US,en;q=0.9','referer':'https://accounts.google.com/','upgrade-insecure-requests':'1','user-agent':ua(),'x-browser-channel':'stable','x-browser-copyright':'Copyright 2024 Google LLC. All rights reserved.','x-browser-year':'2024'}
        params={'biz':'false','continue':'https://mail.google.com/mail/u/0/','ddm':'1','emr':'1','flowEntry':'SignUp','flowName':'GlifWebSignIn','followup':'https://mail.google.com/mail/u/0/','osid':'1','service':'mail'}
        response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        
        tl=response.url.split('TL=')[1]
        s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
        at = response.text.split('"SNlM0e":"')[1].split('"')[0]
        
        headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':ua(),'x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
        params={'rpcids':'E815hb','source-path':'/lifecycle/steps/signup/name','hl':'en-US','TL':tl,'rt':'c'}
        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)
        s.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, headers=headers, data=data)
        
        params={'rpcids':'NHJMOd','source-path':'/lifecycle/steps/signup/username','hl':'en-US','TL':tl,'rt':'c'}
        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(username,at)
        response = s.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, headers=headers, data=data).text
        
        if "password" in response:
            with lock: email_good += 1
            elia_innnn()
            return True
        else:
            with lock: email_bad += 1
            elia_innnn()
            return False
    except:
        with lock: email_bad += 1
        elia_innnn()
        return False

def check_tiktok_real(username):
    """
    التحقق الحقيقي من وجود الحساب وعدد المتابعين
    """
    global tiktok_good, tiktok_bad
    try:
        url = f"https://www.tiktok.com/@{username}"
        headers = {
            "User-Agent": ua(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5"
        }
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # استخراج عدد المتابعين من الـ script tag (JSON)
            match = re.search(r'"followerCount":(\d+)', response.text)
            if match:
                followers = int(match.group(1))
                if followers >= 1000:
                    with lock: tiktok_good += 1
                    elia_innnn()
                    # إذا الحساب قوي، نفحص البريد
                    if gmail_elia(f"{username}@gmail.com"):
                        elia88(username, followers)
                else:
                    with lock: tiktok_bad += 1
                    elia_innnn()
            else:
                with lock: tiktok_bad += 1
                elia_innnn()
        else:
            with lock: tiktok_bad += 1
            elia_innnn()
    except:
        with lock: tiktok_bad += 1
        elia_innnn()

def elia12():
    # أنماط يوزرات تزيد من احتمالية الصيد (كلمات شائعة + حروف)
    words = ["user", "admin", "star", "dark", "pro", "king", "light", "love", "life"]
    while True:
        base = random.choice(words)
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 3)))
        username = base + suffix
        check_tiktok_real(username)
        time.sleep(random.uniform(0.5, 1.0))

# تشغيل
threads_count = 10
for i in range(threads_count):
    t = Thread(target=elia12)
    t.daemon = True
    t.start()

while True:
    time.sleep(1)
