FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY apiserver/ .

# RUN pip install --no-cache-dir --ignore-installed six -r requirements.txt