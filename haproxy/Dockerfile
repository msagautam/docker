from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y haproxy

WORKDIR /root

COPY haproxy.cfg /etc/haproxy
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
