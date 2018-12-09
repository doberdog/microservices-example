#!/bin/bash
set -e

POSTGRES="psql --username ${POSTGRES_USER}"

echo "Creating Petrichor databases..."
$POSTGRES <<EOSQL
CREATE DATABASE ${WEATHER_SERVICE_DB_NAME} OWNER ${APP_USER};
CREATE DATABASE ${LOG_SERVICE_DB_NAME} OWNER ${APP_USER};
EOSQL
