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

# Stats and Lock for thread safety
lock = Lock()
tiktok_good = 0
tiktok_bad = 0
email_good = 0
email_bad = 0

def elia5():
    sd = random.choice([J1, J2, J21, J22, F1, C1, P1, P2])
    os.system('clear||cls')
    banner = f"""{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22} [𝑬𝑳𝑰𝑨] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{sd}
         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝

        {X}¸.•´¯`•.¸¸ {F} [꧁ 𝑬𝑳𝑰𝑨 - 𝑻𝑰𝑲𝑻𝑶𝑲 ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}TLE : @ELIA_py / @XRRHX
{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22} [𝑬𝑳𝑰𝑨] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
    print(banner)

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

def check_gmail_availability(username):
    """
    منطق متقدم لفحص توفر بريد جيميل للتسجيل.
    """
    try:
        email = f"{username}@gmail.com"
        # استخدام رابط التحقق المباشر من جوجل
        url = f"https://mail.google.com/mail/gxlu?email={email}"
        headers = {'User-Agent': ua()}
        res = requests.get(url, headers=headers, timeout=10)
        # إذا لم يتم العثور على البريد في جوجل، فإنه متاح للتسجيل
        if 'Set-Cookie' not in res.headers:
            return True
    except:
        pass
    return False

def get_tiktok_info(username):
    global tiktok_good, tiktok_bad, email_good, email_bad
    try:
        url = f"https://www.tiktok.com/@{username}"
        # هيدرز حقيقية لتجنب الحظر
        headers = {
            "User-Agent": ua(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # استخراج عدد المتابعين بدقة من الـ HTML
            # تيك توك يضع البيانات في كود JSON داخل script tag
            match = re.search(r'"followerCount":(\d+)', response.text)
            if match:
                followers = int(match.group(1))
                if followers >= 1000:
                    with lock: tiktok_good += 1
                    elia_innnn()
                    
                    # فحص توفر البريد
                    if check_gmail_availability(username):
                        with lock: email_good += 1
                        elia_innnn()
                        elia88(username, followers)
                    else:
                        with lock: email_bad += 1
                        elia_innnn()
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
    # قائمة بكلمات شائعة أو أنماط يوزرات قديمة
    patterns = ["user", "admin", "king", "pro", "star", "dark", "light", "love", "life"]
    while True:
        # توليد يوزر ذكي: كلمة شائعة + أرقام أو حروف عشوائية
        base = random.choice(patterns)
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 3)))
        username = base + suffix
        get_tiktok_info(username)
        # تأخير بسيط لتجنب حظر الآي بي
        time.sleep(random.uniform(0.5, 1.5))

# تشغيل الخيوط بعدد معقول لتجنب الحظر وتداخل الشاشة
elia5()
threads_count = 5
for i in range(threads_count):
    t = Thread(target=elia12)
    t.daemon = True
    t.start()

# إبقاء السكريبت يعمل
while True:
    time.sleep(1)
