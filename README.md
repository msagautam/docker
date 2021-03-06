# docker

Tag it with myapp 1.0
docker build . -t myapp:1.0

run iteractive, allocate psuedo tty, delete container after exit
docker run -it --rm --name apptest1 myapp:1.0

Container inspect
docker container inspect apptest1

Stop running container
docker stop apptest1

Delete container
docker container rm apptest1

Delete image
docker image rm myapp:1.0

List running containers and images
docker ps -a
docker images

compose rebuild docker images and spawn 2 "web" services
docker-compose up --scale web=2 --build
docker container rm docker_web_1 docker_web_2 docker_db_1 docker_dbadmin_1 docker_proxy_1 docker_monitor_1 docker_graph_1
docker rmi docker_web:latest docker_db:latest docker_proxy:latest docker_monitor:latest

list all containers ipaddresses
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }} {{range .NetworkSettings.Networks}} {{.IPAddress}}{{end}}' | sed 's#^/##';

Remove all stopped containers, dangling images, networks, cache
docker system prune

# Read apache2 logs, usually present in /var/log/apache2 folder
cat /var/log/apache2/error.log

# Test web service latencies using apache bench
ab -c 1000 -n 10000 <test_website>
# Memory and CPU usage
sar -ur <seconds>

#Upload to dockerhub
docker login
docker push mgautam/myapp:1.0

#Tag git
git commit -m "commit before tag"
git tag -a v1.0 -m "version 1.0"
git push origin v1.0
git push
#Delete Tag
git tag -d v1.0
git push --delete origin v1.0

