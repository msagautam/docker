docker build --tag haproxy:1.0 .
docker run -it --rm --name proxytest1 haproxy:1.0

haproxy_exporter publishes on port 9101
haproxy publishes /stats;csv on port 8404 and also redirects :8404/metrics to 9101/metrics
