from typing import Any

import aiohttp


async def get_response(host: str, port: int, timeout: float = 1.0) -> Any:
    uri = "/api/v1/hello"
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
        async with session.get(f"http://{host}:{port}{uri}", data="{}") as response:
            status = response.status
            assert status == 200, status
            ret = await response.text()
            return ret
