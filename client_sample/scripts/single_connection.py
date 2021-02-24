#!/usr/bin/env python3

import asyncio

from client_sample import get_response


async def main() -> None:
    ret = await get_response(host="localhost", port=9000)
    print("reponse : ", ret)


if __name__ in "__main__":
    asyncio.run(main())
