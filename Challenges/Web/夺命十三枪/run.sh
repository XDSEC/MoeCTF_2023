#/bin/bash

echo "export FLAG=$FLAG" >> /etc/apache2/envvars

service apache2 start

while true; do
    sleep 30
    echo "Keeping Alive..."
done;