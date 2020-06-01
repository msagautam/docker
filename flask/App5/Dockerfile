from ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential python3-pip
RUN apt-get install -y uwsgi uwsgi-plugin-python
RUN apt-get install -y curl
RUN apt-get install -y nginx

WORKDIR /root

COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY myfilesApp.conf /etc/nginx/sites-available/
COPY uwsgi.ini /etc/uwsgi/apps-available/
ADD myfilesApp /var/www/myfilesApp
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
