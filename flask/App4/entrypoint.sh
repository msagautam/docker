#!/bin/bash

service apache2 start

a2dissite 000-default.conf
a2ensite myfilesApp
service apache2 reload

#service apache2 restart

cd /var/www/
mkdir upload_data_files
chmod 777 upload_data_files
#python3 -m myfilesApp 

#export FLASK_APP=myfilesApp
#flask run

# For interactive terminal
#/bin/bash

# For never ending program
tail -f /var/log/apache2/*
