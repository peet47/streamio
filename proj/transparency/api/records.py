import aiohttp
import asyncio

class Records:
    def __init__(self, source):
        self.timeout = aiohttp.ClientTimeout(total=10)
        self.source = source

    async def request(self, session, url):
        async with session.get(url) as response:
            return await response.json()
        
    async def get(self, min_records, max_records):
        url = 'http://{0}ct/v1/get-entries?start={1}&end={2}'.format(self.source, min_records, max_records)
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            response = await self.request(session, url)
            return response

    async def latest(self):
        url = 'http://{0}ct/v1/get-sth'.format(self.source)
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            response = await self.request(session, url)
            return response
