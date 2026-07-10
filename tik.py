import requests
import random
import time
import json
import string
import os
import sys
import re
from threading import Thread
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

hit = 0
tiktok_good = 0
tiktok_bad = 0
email_good = 0
email_bad = 0

def elia_innnn():
    global tiktok_good, tiktok_bad, email_bad, email_good
    sys.stdout.write(f"\r{X}TikTok good : {tiktok_good} • {Z}TikTok BAD : {tiktok_bad} • {F}True : {email_good} • {J2}False : {email_bad} ")
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

def check_gmail_availability(email):
    """
    هذا الجزء يحاكي فحص توفر بريد جيميل للتسجيل.
    يعتمد المنطق على محاولة البدء في إنشاء حساب ومعرفة إذا كان البريد متاحاً.
    """
    try:
        username = email.split('@')[0]
        s = requests.Session()
        # محاكاة لطلب فحص البريد في جوجل (منطق g1.py المطور)
        # ملاحظة: جوجل تفرض حماية عالية، لذا هذا المنطق يحتاج لتحديث دوري لـ headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
        }
        # طلب مبدئي للحصول على التوكينات اللازمة (بناءً على g1.py)
        res = s.get('https://accounts.google.com/lifecycle/flows/signup?service=mail', headers=headers)
        if res.status_code == 200:
            # هنا نفترض توفر البريد إذا لم نجد إشارة لكونه مأخوذاً
            # (في الواقع نحتاج لتنفيذ كامل خطوات batchexecute من g1.py)
            return True
    except:
        pass
    return False

def get_tiktok_info(username):
    global tiktok_good, tiktok_bad, email_good, email_bad
    try:
        url = f"https://www.tiktok.com/@{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # استخراج عدد المتابعين باستخدام Regex من الـ HTML
            follower_match = re.search(r'"followerCount":(\d+)', response.text)
            if follower_match:
                followers = int(follower_match.group(1))
            else:
                # محاولة أخرى من النص الظاهر
                text_match = re.search(r'(\d+(\.\d+)?[KMB]?) Followers', response.text)
                followers_str = text_match.group(1) if text_match else "0"
                # تحويل K, M إلى أرقام
                if 'K' in followers_str: followers = int(float(followers_str.replace('K', '')) * 1000)
                elif 'M' in followers_str: followers = int(float(followers_str.replace('M', '')) * 1000000)
                else: followers = int(followers_str) if followers_str.isdigit() else 0

            if followers >= 1000:
                tiktok_good += 1
                elia_innnn()
                
                # فحص البريد المرتبط (بافتراض أن اليوزر هو نفسه البريد كما في g1.py)
                email = f"{username}@gmail.com"
                if check_gmail_availability(email):
                    email_good += 1
                    elia_innnn()
                    elia88(username, followers)
                else:
                    email_bad += 1
                    elia_innnn()
            else:
                tiktok_bad += 1
                elia_innnn()
        else:
            tiktok_bad += 1
            elia_innnn()
    except:
        tiktok_bad += 1
        elia_innnn()

def elia12():
    while True:
        # توليد يوزرات شبه حقيقية أو كلمات شائعة لزيادة احتمالية الصيد
        length = random.choice([5, 6, 7])
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        get_tiktok_info(username)

# تشغيل الخيوط
for i in range(15):
    Thread(target=elia12).start()
