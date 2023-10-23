#!/bin/sh
python doggy.py $(cat /flag) &
sleep 1
rm /flag
socat tcp-l:9999,fork,reuseaddr exec:"python yourcat.py"
exit 1
