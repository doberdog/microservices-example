FROM postgres:11.1-alpine
COPY ./create_user.sh   /docker-entrypoint-initdb.d/10-create_user.sh
COPY ./create_db.sh     /docker-entrypoint-initdb.d/20-create_db.sh
