#!/bin/bash
service ssh start
redis-server /etc/redis/redis.conf
# 检测 SSH 服务状态
while true; do
    ssh_status=$(service ssh status)

    if [ "$ssh_status" = "sshd is running." ]; then
        echo "SSH 服务已经开启."
        break
    else
        # 启动 SSH 服务
        echo "启动 SSH 服务..."
        sleep 5 
        service ssh start
    fi
done
