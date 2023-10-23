#!/bin/sh
echo $FLAG > /flag
unset FLAG
exec sh startup2.sh
