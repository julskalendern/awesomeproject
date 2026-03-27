FROM python:3.11-slim

RUN mkdir -p /srv/app/conf

COPY web.py /srv/app/web.py
COPY web.conf /srv/app/conf/web.conf

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /srv

CMD ["python","app/web.py"]


