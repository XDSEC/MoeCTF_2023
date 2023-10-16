#/bin/bash

echo "export FLAG=$FLAG" >> /etc/apache2/envvars

service apache2 start

while true; do
    echo "keeping alive...."
    sleep 30
done