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

Docker compose rebuild docker images and spawn 2 "web" services
docker-compose up --scale web=2 --build

