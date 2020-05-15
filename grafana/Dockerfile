from ubuntu:18:04

RUN apt-get install -y apt-transport-https software-properties-common wget
RUN wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

# Alternatively you can add the beta repository, see in the table above
RUN add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"

RUN apt-get update
RUN apt-get install grafana


