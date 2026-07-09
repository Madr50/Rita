import asyncio
import httpx
from typing import List, Dict, Any, Optional

from src.logger import logger
from src.proxy_manager import ProxyManager

class DataHunter:
    def __init__(self, apis: List[Dict[str, str]], proxy_manager: ProxyManager, max_concurrent_requests: int = 10):
        self.apis = apis
        self.proxy_manager = proxy_manager
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)
        self.client = httpx.AsyncClient()

    async def _make_request(self, api_config: Dict[str, str], query: str) -> Optional[Dict[str, Any]]:
        url = api_config["url"].format(query=query)
        method = api_config.get("method", "GET")
        headers = api_config.get("headers", {})
        body = api_config.get("body")

        proxy = self.proxy_manager.get_next_proxy()
        proxies = {"all": proxy} if proxy else None

        try:
            async with self.semaphore:
                logger.info(f"Making {method} request to {url} with proxy {proxy}")
                response = await self.client.request(method, url, headers=headers, json=body, proxies=proxies, timeout=10)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            logger.error(f"Request to {url} failed: {e}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred during request to {url}: {e}")
            return None

    async def hunt_data(self, query: str) -> List[Dict[str, Any]]:
        results = []
        tasks = []
        for api_config in self.apis:
            tasks.append(self._make_request(api_config, query))
        
        # Run requests concurrently
        api_responses = await asyncio.gather(*tasks)

        for response in api_responses:
            if response:
                results.append(response)
        return results

# Example API configurations (to be moved to config later)
sample_apis = [
    {
        "name": "Example API 1",
        "url": "https://api.example.com/search?q={query}",
        "method": "GET",
        "headers": {"Authorization": "Bearer YOUR_API_KEY"}
    },
    {
        "name": "Example API 2",
        "url": "https://api.anotherservice.com/data",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": {"search_term": "{query}"}
    }
]

async def main():
    # Placeholder for proxy manager initialization
    proxy_list = ["http://user:pass@1.2.3.4:8080", "socks5://user:pass@5.6.7.8:1080"]
    proxy_manager = ProxyManager(proxy_list)
    
    hunter = DataHunter(sample_apis, proxy_manager)
    query = "test_data"
    results = await hunter.hunt_data(query)
    logger.info(f"Hunt results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
