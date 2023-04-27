FROM mysql:latest

ENV MYSQL_DATABASE=test
ENV MYSQL_ROOT_PASSWORD totallysecurepass
ADD init.sql /docker-entrypoint-initdb.d

EXPOSE 3306
