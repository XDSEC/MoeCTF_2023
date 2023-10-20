FROM ubuntu:22.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin

COPY ./build/ctf.xinetd /etc/xinetd.d/ctf
COPY ./build/start.sh /start.sh

RUN chown root:root /etc/xinetd.d/ctf && \
    chown root:root /start.sh && \
    chmod 400 /etc/xinetd.d/ctf && \
    chmod 500 /start.sh

COPY ./build/pwn /home/ctf/
COPY ./build/flag /home/ctf/

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag

CMD ["/start.sh"]

EXPOSE 9999
