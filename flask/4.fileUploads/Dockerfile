from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y apache2 libapache2-mod-wsgi-py3 python3-pip
RUN apt-get install -y curl

WORKDIR /root

COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY myfilesApp.conf /etc/apache2/sites-available/
ADD myfilesApp /var/www/myfilesApp
COPY myfilesApp.wsgi /var/www/
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
