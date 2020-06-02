#!/bin/bash

cd /etc/nginx/
mkdir ssl
chmod 700 ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/myssl.key -out /etc/nginx/ssl/myssl.crt -subj "/C=AU/ST=Victoria/L=Melbourne/O=Certificate Company/OU=IT Department/CN=myServer/E=test@email.com"

rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/helloApp.conf /etc/nginx/sites-enabled/
service nginx restart

service uwsgi stop
ln -s /etc/uwsgi/apps-available/uwsgi.ini /etc/uwsgi/apps-enabled/
#service uwsgi restart
nohup uwsgi /etc/uwsgi/apps-enabled/uwsgi.ini 

usermod -a -G www-data www-data
chown -R www-data:www-data /tmp/

#uwsgi /etc/uwsgi/apps-available/uwsgi.ini

#python3 -m helloApp

#export FLASK_APP=helloApp
#flask run

# For interactive terminal
#/bin/bash

# For never ending program
tail -f /var/log/nginx/helloApp.log
#tail -f /var/log/uwsgi/*
#uwsgi --http-socket :8080 --plugin python -w helloApp:app
