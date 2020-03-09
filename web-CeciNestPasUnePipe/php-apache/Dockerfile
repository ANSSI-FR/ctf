FROM php:7.3.4-apache-stretch
RUN docker-php-ext-install mysqli pdo_mysql exif
COPY ./www/ /var/www/html/
RUN chown -R root:root /var/www/html/
RUN chmod -R 755 /var/www/html/
RUN chmod a+t /var/www/html/upload/
RUN chmod 733 /var/www/html/upload/
RUN touch /var/www/html/.htaccess /var/www/html/upload/.htaccess
RUN chmod 444 /var/www/html/.htaccess /var/www/html/upload/.htaccess
RUN chmod +x /home
COPY ./conf/sendmail/sendmail /usr/sbin/sendmail
RUN mkdir -p /usr/share/php/chall
COPY ./conf/php/prepend.php /usr/share/php/chall
COPY ./conf/php/php.ini /usr/local/etc/php
RUN mkdir -p /var/lib/php/sessions && chmod 1733 /var/lib/php/sessions
RUN find /var/www/html -name ".git*" -exec rm -rf {} \;
COPY ./conf/flag/flag /home/flag
RUN chmod a-r /home/flag
