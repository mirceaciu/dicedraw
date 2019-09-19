FROM jjanzic/docker-python3-opencv:latest

RUN apt-get update -y

COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY ./compose/server/run.sh /app/run.sh

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV HOME=/app
WORKDIR /app
ENV PYTHONPATH=/app
ENV FLASK_MP=wsgi.py

RUN mkdir -p /var/log/gunicorn \
    && touch /var/log/gunicorn/error.log && chmod 666 /var/log/gunicorn/error.log \ 
    && touch /var/log/gunicorn/access.log && chmod 666 /var/log/gunicorn/access.log

RUN chmod +x run.sh

EXPOSE 5000
ENTRYPOINT ["./run.sh"]
