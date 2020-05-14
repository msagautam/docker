docker build -t myprome:1.0 .
docker run -it --rm --name promtest1 myprome:1.0 --config.file=/etc/prometheus/prometheus.yml
