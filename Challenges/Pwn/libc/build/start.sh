#!/bin/sh

echo $FLAG > /home/ctf/flag
export FLAG=
/etc/init.d/xinetd start
sleep infinity
