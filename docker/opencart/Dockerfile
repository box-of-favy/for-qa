# Используем образ Ubuntu 18.04
FROM ubuntu:bionic

# Устанавливаем переменные окружения для автоматизации диалоговых окон
ENV DEBIAN_FRONTEND=noninteractive 

# Обновляем пакеты и устанавливаем необходимое программное обеспечение
RUN apt-get update \
 && apt-get install -y apache2 mariadb-server mariadb-client php libapache2-mod-php php-cli php-common php-mbstring php-gd php-intl php-xml php-mysql php-zip php-curl php-xmlrpc unzip wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Конфигурируем Apache
RUN sed -i "s/Options Indexes FollowSymLinks/Options FollowSymLinks/" /etc/apache2/apache2.conf

# Конфигурируем MariaDB
COPY setup.sql /setup.sql
RUN service mysql start \
 && mysql -u root < /setup.sql

# Скачиваем и распаковываем OpenCart
RUN wget https://github.com/opencart/opencart/releases/download/3.0.3.1/opencart-3.0.3.1.zip -P /tmp \
 && unzip /tmp/opencart-*.zip -d /tmp \
 && mv /tmp/upload/ /var/www/html/opencart \
 && cp /var/www/html/opencart/config-dist.php /var/www/html/opencart/config.php \
 && cp /var/www/html/opencart/admin/config-dist.php /var/www/html/opencart/admin/config.php \
 && chown -R www-data:www-data /var/www/html/opencart/ \
 && chmod -R 755 /var/www/html/opencart/

# Настраиваем VirtualHost
COPY opencart.conf /etc/apache2/sites-available/opencart.conf
RUN a2ensite opencart.conf \
 && a2enmod rewrite \
 && service apache2 restart

# Открываем порт 80 для подключений к Apache
EXPOSE 80

# Запускаем Apache и MariaDB при старте контейнера
CMD service mysql start && apachectl -D FOREGROUND
