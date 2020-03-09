FROM php:7.3.4-apache-stretch

COPY ./www/ /var/www/html/
RUN chmod a-w /var/www/html/
RUN chmod +x /home
RUN mkdir -p /usr/share/php/chall

COPY ./conf/php/prepend.php /usr/share/php/chall
COPY ./conf/php/php.ini /usr/local/etc/php
COPY ./conf/flag/flag.txt /home/flag.txt

EXPOSE 80
