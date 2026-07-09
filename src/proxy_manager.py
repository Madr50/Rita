import httpx
import asyncio
import random
from typing import List, Dict, Optional

from logger import logger

class ProxyManager:
    def __init__(self, proxies: List[str]):
        self.proxies = proxies
        self.current_proxy_index = 0
        if self.proxies:
            random.shuffle(self.proxies)

    def get_next_proxy(self) -> Optional[str]:
        if not self.proxies:
            return None
        proxy = self.proxies[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxies)
        return proxy

    async def test_proxy(self, proxy: str, timeout: int = 5) -> bool:
        try:
            async with httpx.AsyncClient(proxies={"all": proxy}, timeout=timeout) as client:
                response = await client.get("https://api.ipify.org?format=json")
                response.raise_for_status()
                logger.info(f"Proxy {proxy} is working. IP: {response.json().get("ip")}")
                return True
        except httpx.RequestError as e:
            logger.warning(f"Proxy {proxy} failed: {e}")
            return False

    async def get_working_proxy(self) -> Optional[str]:
        if not self.proxies:
            logger.warning("No proxies configured.")
            return None

        for _ in range(len(self.proxies)): # Try all proxies once
            proxy = self.get_next_proxy()
            if proxy and await self.test_proxy(proxy):
                return proxy
        logger.error("No working proxies found after testing all configured proxies.")
        return None

# Example usage (for testing purposes)
async def main():
    # Example proxies (replace with actual proxies)
    test_proxies = [
        "http://user:pass@1.2.3.4:8080",
        "socks5://user:pass@5.6.7.8:1080",
    ]
    proxy_manager = ProxyManager(test_proxies)

    logger.info("Testing proxies...")
    working_proxy = await proxy_manager.get_working_proxy()
    if working_proxy:
        logger.info(f"Found working proxy: {working_proxy}")
    else:
        logger.info("No working proxies found.")

if __name__ == "__main__":
    asyncio.run(main())
