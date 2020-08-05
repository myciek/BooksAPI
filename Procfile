release: python manage.py migrate
release: python manage.py flush --no-input
release: python manage.py loaddata initial_data.json
web: gunicorn booksapi.wsgi