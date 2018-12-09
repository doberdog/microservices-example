#!/bin/bash
set -e

POSTGRES="psql --username postgres"

echo "Creating database role: petrichor"

${POSTGRES} <<-EOSQL
CREATE USER petrichor WITH PASSWORD 'petrichor';
EOSQL
