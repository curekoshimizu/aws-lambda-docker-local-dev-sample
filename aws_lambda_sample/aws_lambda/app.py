from typing import Any, Dict

from aws_lambda_typing import Context  # type: ignore

LambdaDict = Dict[str, Any]


def lambda_handler(event: LambdaDict, context: Context) -> Any:
    print("event : ", event)
    print("context : ", context)
    return "hello world"
