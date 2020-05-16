from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y apache2 libapache2-mod-wsgi-py3 python3-pip
RUN apt-get install -y curl
RUN apt-get install -y vim

WORKDIR /root

COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY mysqlApp.conf /etc/apache2/sites-available/
ADD mysqlApp /var/www/mysqlApp
COPY mysqlApp.wsgi /var/www/
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
