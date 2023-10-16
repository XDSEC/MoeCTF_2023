#/bin/bash

echo $FLAG > /flag

service apache2 start

while true; do
    echo "keeping alive...."
    sleep 30
done