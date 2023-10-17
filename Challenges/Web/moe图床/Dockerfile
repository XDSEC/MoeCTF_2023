FROM webimp/php-72-apache

COPY run.sh /

COPY index.html /var/www/html/
COPY upload.php /var/www/html/
RUN mkdir /var/www/html/uploads
RUN chmod 755 /var/www/html/upload.php
RUN chmod -R 777 /var/www/html/uploads

EXPOSE 80
CMD [ "bash", "/run.sh" ]
