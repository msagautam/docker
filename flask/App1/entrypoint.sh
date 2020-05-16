#!/bin/bash

service apache2 start

a2dissite 000-default.conf
a2ensite firstApp
service apache2 reload

#service apache2 restart

cd /var/www/
#python3 -m AssignmentsApp 

#export FLASK_APP=AssignmentsApp
#flask run

# For interactive terminal
#/bin/bash

# For never ending program
tail -f /var/log/apache2/*
