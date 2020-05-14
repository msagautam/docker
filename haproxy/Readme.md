docker build --tag haproxy:1.0 .
docker run -it --rm --name proxytest1 haproxy:1.0
