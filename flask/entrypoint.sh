#!/bin/bash

a2ensite AssignmentsApp
service apache2 reload

cp /var/www/flaskapp.wsgi /home/
service apache2 restart

cd /var/www/
python3 -m AssignmentsApp 

#export FLASK_APP=AssignmentsApp
#flask run

#/bin/bash
