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

/bin/bash
