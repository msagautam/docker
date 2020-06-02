#!/bin/bash

service apache2 start

a2dissite 000-default.conf
a2ensite PackagedApp
service apache2 reload

#service apache2 restart

cd /var/www/
#python3 -m PackagedApp 

#export FLASK_APP=PackagedApp
#flask run

# For interactive terminal
#/bin/bash

# For never ending program
tail -f /var/log/apache2/*
