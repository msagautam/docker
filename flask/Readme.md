# docker

Tag it with myapp 1.0
docker build . -t myapp:1.0

run iteractive, allocate psuedo tty, delete container after exit
docker run -it --rm --name apptest1 myapp:1.0

