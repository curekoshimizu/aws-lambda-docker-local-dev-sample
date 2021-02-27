# aws-lambda-docker-local-dev-sample

[AWS Lambda](https://github.com/lambci/docker-lambda) supports to develop AWS Lambda Docker locally.
But, it does not support multiple connection feature.

This sample code adds a load balancer to provide a mutex lock for docker-lambda.


## How to use

```
docker-compose up -d
cd ./client_sample
poetry install
poetry run ./scripts/multi_connection.py
```

# LICENSE

MIT LICENSE
