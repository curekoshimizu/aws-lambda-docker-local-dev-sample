#!/usr/bin/env python3

import asyncio

from client_sample import get_response


async def main() -> None:
    port = 9001
    ret = await asyncio.gather(get_response(host="localhost", port=port), get_response(host="localhost", port=port))
    print("reponse : ", ret)


if __name__ in "__main__":
    asyncio.run(main())
