#!/bin/bash

service haproxy restart

WORKDIR /root

#wget https://github.com/prometheus/haproxy_exporter/releases/download/v0.10.0/haproxy_exporter-0.10.0.linux-amd64.tar.gz
tar xzvf haproxy_exporter-0.10.0.linux-amd64.tar.gz
./haproxy_exporter-0.10.0.linux-amd64/haproxy_exporter

#/bin/bash
