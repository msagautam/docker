# docker

Tag it with myapp 1.0
docker build . -t myapp:1.0

run iteractive, allocate psuedo tty, delete container after exit
docker run -it --rm --name apptest1 myapp:1.0

# Apache2 configuration
apt install -y libapache2-mod-wsgi-py3
copy firstApp.conf to /etc/apache2/sites-available/
a2dissite 000-default.conf
a2ensite firstApp.conf
service apache2 reload
