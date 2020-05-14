from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y apache2 libapache2-mod-wsgi python3-pip
RUN apt-get install -y curl

WORKDIR /root

COPY flaskApps/requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY flaskApps /var/www/
COPY AssignmentsApp.conf /etc/apache2/sites-available/
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
