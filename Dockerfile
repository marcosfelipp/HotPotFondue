FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --ignore-installed six -r requirements.txt
COPY uwsgi.ini .
COPY settings.toml .

COPY hotpot hotpot/

ENV STATIC_PATH /app/hotpot/static

EXPOSE 80:80