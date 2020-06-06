#!/bin/bash

mkdir -p /root/generalshare
chown nobody:nogroup /root/generalshare
chmod 777 /root/generalshare

echo "/root/generalshare 172.17.0.0/16(rw,sync,no_subtree_check)" >> /etc/exports

exportfs -a
service nfs-kernel-server restart

ufw allow 2049

/bin/bash
