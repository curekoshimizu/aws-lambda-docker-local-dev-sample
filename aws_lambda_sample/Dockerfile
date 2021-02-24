FROM public.ecr.aws/lambda/python:3.8 AS requirement_txt
RUN pip3 install --upgrade pip

ARG POETRY_VERSION=1.1.4
RUN pip3 install poetry==${POETRY_VERSION}

COPY poetry.lock pyproject.toml setup.py ./
RUN poetry export > /requirement.txt



FROM public.ecr.aws/lambda/python:3.8
RUN echo "Asia/Tokyo" > /etc/timezone \
        && rm /etc/localtime \
        && ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN pip install --upgrade pip

WORKDIR /opt
COPY --from=requirement_txt /requirement.txt requirement.txt
RUN pip install -r requirement.txt  \
        && rm requirement.txt

COPY pyproject.toml setup.py ./
COPY aws_lambda/ aws_lambda/
RUN pip install .

CMD ["aws_lambda.app.lambda_handler"]
