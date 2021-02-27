import threading
from typing import Any

import requests

lock = threading.Lock()


def hello_world(
    host: str = "aws_lambda",
    port: int = 8080,
) -> Any:
    with lock:
        ret = requests.post(f"http://{host}:{port}/2015-03-31/functions/function/invocations", data="{}")
    return ret.json()
