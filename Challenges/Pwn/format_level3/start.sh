#!/bin/sh
# Add your startup script

echo $FLAG > /home/ctf/flag
export FLAG=
# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
