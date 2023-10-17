FROM vulhub/php-xxe

COPY index.php /var/www/html
COPY moectf.jpg /var/www/html
COPY Viper.jpg /var/www/html
COPY Viper1.jpg /var/www/html

COPY rx7.jpg /var/www/html
COPY rx7-1.jpg /var/www/html
COPY rx7-2.jpg /var/www/html

COPY rtr.jpg /var/www/html
COPY rtr1.jpg /var/www/html

COPY r35.jpg /var/www/html
COPY r35-1.jpg /var/www/html

COPY 86.jpg /var/www/html
COPY 86-1.jpg /var/www/html

COPY 36.jpg /var/www/html
COPY 36-1.jpg /var/www/html

COPY o_o.jpg /var/www/html

COPY run.sh /

RUN chmod 777 /run.sh

EXPOSE 80:80

CMD [ "bash", "/run.sh" ]