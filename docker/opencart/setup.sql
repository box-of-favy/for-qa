   CREATE DATABASE opencart;
   CREATE USER 'ocuser'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON opencart.* TO 'ocuser'@'localhost';
   FLUSH PRIVILEGES;