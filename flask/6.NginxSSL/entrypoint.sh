#!/bin/bash

cd /etc/nginx/
#mkdir ssl
chmod 700 ssl
#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/myssl.key -out /etc/nginx/ssl/myssl.crt -subj "/C=AU/ST=Victoria/L=Melbourne/O=Certificate Company/OU=IT Department/CN=myServer/E=test@email.com"

rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/k6proxy.conf /etc/nginx/sites-enabled/
service nginx restart

service uwsgi stop
ln -s /etc/uwsgi/apps-available/uwsgi.ini /etc/uwsgi/apps-enabled/
#service uwsgi restart
nohup uwsgi /etc/uwsgi/apps-enabled/uwsgi.ini 


# For never ending program
tail -f /var/log/nginx/k6proxy.log
