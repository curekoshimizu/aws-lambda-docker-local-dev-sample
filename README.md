# aws-lambda-docker-local-dev-sample

[AWS Lambda](https://github.com/lambci/docker-lambda) supports to develop AWS Lambda Docker locally.
But, it does not support multiple connection feature.

This sample code adds a load balancer to provide a mutex lock for docker-lambda.

If you remove [mutex lock](https://github.com/curekoshimizu/aws-lambda-docker-local-dev-sample/blob/main/docker_src/balancer/balancer/api.py#L13),
you can notice that AWS Lambda has not support multiple connection feature yet.


## How to use

```
docker-compose up -d
cd ./client_sample
poetry install
poetry run ./scripts/multi_connection.py
```

## Connection

client_sample --> balancer (just bypass with mutex lock) --> aws_lambda

# LICENSE

MIT LICENSE
