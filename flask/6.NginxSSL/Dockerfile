from ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential python3-pip
RUN apt-get install -y uwsgi uwsgi-plugin-python
RUN apt-get install -y nginx
RUN apt-get install -y curl vim

WORKDIR /root

COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY helloApp.conf /etc/nginx/sites-available/
COPY uwsgi.ini /etc/uwsgi/apps-available/
ADD helloApp /var/www/helloApp
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
