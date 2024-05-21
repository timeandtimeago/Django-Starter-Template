#!/bin/bash
echo "Running DEVELOPMENT Entrypoint..."
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#python manage.py flush --no-input #NOTE: This line clears all DB data.
#echo "make migrations"
#python manage.py makemigrations
echo "migrate"
python manage.py migrate

exec "$@"