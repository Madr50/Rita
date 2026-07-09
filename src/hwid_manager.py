import hashlib
import platform
import os
from .logger import logger

HWID_FILE = 'config/hwid.key'

def generate_hwid():
    # In a real scenario, this would generate a unique ID based on hardware.
    # For demonstration, we'll use a combination of system info.
    system_info = f"{platform.node()}-{platform.system()}-{platform.machine()}-{platform.processor()}"
    return hashlib.sha256(system_info.encode()).hexdigest()

def save_hwid(hwid: str):
    with open(HWID_FILE, 'w') as f:
        f.write(hwid)

def load_hwid():
    if os.path.exists(HWID_FILE):
        with open(HWID_FILE, 'r') as f:
            return f.read().strip()
    return None

def check_hwid(allowed_hwid: str | None = None) -> bool:
    current_hwid = generate_hwid()
    if not os.path.exists(HWID_FILE):
        save_hwid(current_hwid)
        logger.info(f"[HWID Manager] Generated and saved new HWID: {current_hwid}")
        return True # First run, allow access

    saved_hwid = load_hwid()

    if allowed_hwid and saved_hwid == allowed_hwid:
        logger.info(f"[HWID Manager] HWID matched with provided allowed HWID: {saved_hwid}")
        return True
    elif not allowed_hwid and saved_hwid == current_hwid:
        logger.info(f"[HWID Manager] HWID matched with saved HWID: {saved_hwid}")
        return True
    else:
        logger.critical(f"[HWID Manager] HWID mismatch! Current: {current_hwid}, Saved: {saved_hwid}, Allowed: {allowed_hwid}")
        return False
