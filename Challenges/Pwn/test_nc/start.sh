#!/bin/sh
# Add your startup script

echo 'Do you know linux hidden file?' > /home/ctf/gift
echo $FLAG > /home/ctf/.flag
export FLAG=
# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
