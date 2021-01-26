FROM python:3-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app


COPY main.py .
COPY tasks.py .

CMD [ "python3", "main.py" ]