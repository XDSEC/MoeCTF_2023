#!/bin/bash

# 服务启动
service apache2 start
service mysql start || true

# 等待MySQL服务启动
echo "Waiting for MySQL to start..."
while ! service mysql status &> /dev/null; do
  sleep 1
done

# MySQL数据库连接配置
DB_HOST="127.0.0.1"
DB_USER="wp_user"
DB_PASS="d6nyPBdjNYmF31EV"
DB_NAME="wordpress"

# 等待MySQL服务启动完成后，再执行MySQL查询
echo "MySQL started. Executing the initial query..."
QUERY="INSERT INTO secret_of_kokomi (content) VALUES ('$FLAG');"
mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" -e "$QUERY"

while true; do
  echo "Reseting flag..."
  UPDATE_QUERY="UPDATE secret_of_kokomi SET content='$FLAG' WHERE id=3;"
  mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" -e "$UPDATE_QUERY"
  sleep 30
done
