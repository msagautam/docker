from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y iputils-ping curl vim
RUN apt-get install -y nfs-kernel-server

WORKDIR /root
COPY ./entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
