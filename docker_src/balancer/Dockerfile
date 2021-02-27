FROM public.ecr.aws/lambda/python:3.8 AS requirement_txt
RUN pip3 install --upgrade pip

ARG POETRY_VERSION=1.1.4
RUN pip3 install poetry==${POETRY_VERSION}

COPY poetry.lock pyproject.toml setup.py ./
RUN poetry export > /requirement.txt


FROM python:3.8.8-slim-buster

WORKDIR /opt
COPY --from=requirement_txt /requirement.txt requirement.txt
RUN pip install -r requirement.txt  \
        && rm requirement.txt

COPY pyproject.toml setup.py ./
COPY balancer/ balancer/
RUN pip install .
COPY scripts/ scripts/

CMD ["./scripts/run_server.py"]
