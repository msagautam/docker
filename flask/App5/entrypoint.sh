#!/bin/bash

cd /var/www/
mkdir upload_data_files
chmod 777 upload_data_files

rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/myfilesApp.conf /etc/nginx/sites-enabled/
ln -s /etc/uwsgi/apps-available/uwsgi.ini /etc/uwsgi/apps-enabled/
service nginx restart
service uwsgi restart

nohup uwsgi /etc/uwsgi/apps-available/uwsgi.ini &

usermod -a -G www-data
chown -R www-data:www-data /tmp/

#python3 -m myfilesApp 

#export FLASK_APP=myfilesApp
#flask run

# For interactive terminal
#/bin/bash

# For never ending program
#tail -f /var/log/uwsgi/*
uwsgi --http-socket :8080 --plugin python -w myfilesApp:app
