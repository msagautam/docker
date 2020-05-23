from ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git iputils-ping curl sudo

WORKDIR /root
COPY ./entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
