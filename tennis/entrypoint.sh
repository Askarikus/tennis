#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Fill database with users
python manage.py fill_users_players

# Fill database with scores
python manage.py fill_scores

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

exec "$@"