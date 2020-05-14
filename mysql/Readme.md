docker build --tag mysql:5.7 mysql-docker/5.7/
docker build --tag mysql:8.0 mysql-docker/8.0/
docker run -it --rm --name sqltest1 -e MYSQL_ROOT_HOST=% -e MYSQL_ROOT_PASSWORD=testpassword -p 3306:3306 mysql:5.7
docker run -it --rm --name sqltest2 -e MYSQL_ROOT_HOST=% -e MYSQL_ROOT_PASSWORD=testpassword -p 3306:3306 mysql:8.0
