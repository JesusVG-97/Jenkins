FROM python:3.10-slim

WORKDIR /app

COPY python/ /app

RUN pip install pytest

CMD ["pytest"]
