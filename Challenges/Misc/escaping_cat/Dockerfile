FROM docker.io/alpine

RUN apk add --no-cache python3 socat

WORKDIR /problem

COPY . .

CMD ["sh", "/problem/startup1.sh"]
