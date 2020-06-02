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


# mount host mysql folder in pwd to /var/www/mysqlApp in container
docker run -it -v "$(pwd)"/mysqlApp:/var/www/mysqlApp --rm myflask:3.0

# To enable development features
export FLASK_ENV=development
flask run --host=0.0.0.0

# Nginx Deployment
nginx -t # Check configuration
/etc/nginx/nginx.conf # Modify global configuration
