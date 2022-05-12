#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


liquibase "--defaultsFile=/liquibase/liquibase.properties" update
echo "Liquibase started"

exec "$@"