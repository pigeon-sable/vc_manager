# syntax=docker/dockerfile:1

FROM python:3.11.3-alpine3.17

WORKDIR /app

COPY ./requirements.txt /app
COPY ./src /app

RUN pip install --no-cache-dir --upgrade pip==23.3.1 && pip install --no-cache-dir -r requirements.txt

CMD ["python", "vc_manager.py"]
