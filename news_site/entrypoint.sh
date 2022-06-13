#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "PostgreSQL started"
#python manage.py makemigrations
#python manage.py migrate

exec "$@"