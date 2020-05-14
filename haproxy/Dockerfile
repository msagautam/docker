from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y haproxy wget

WORKDIR /root
RUN wget https://github.com/prometheus/haproxy_exporter/releases/download/v0.10.0/haproxy_exporter-0.10.0.linux-amd64.tar.gz

COPY haproxy.cfg /etc/haproxy
COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
