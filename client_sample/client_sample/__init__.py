from typing import Any

import aiohttp


async def get_response(host: str, port: int, timeout: float = 1.0) -> Any:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
        async with session.post(
            f"http://{host}:{port}/2015-03-31/functions/function/invocations", data="{}"
        ) as response:
            status = response.status
            assert status == 200, status
            ret = await response.text()
            return ret
