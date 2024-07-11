CREATE DATABASE mywebsite;
CREATE USER 'mywebsiteuser'@'localhost' IDENTIFIED BY 'Stifler@99';
GRANT ALL PRIVILEGES ON mywebsite.* TO 'mywebsiteuser'@'localhost';
FLUSH PRIVILEGES;
