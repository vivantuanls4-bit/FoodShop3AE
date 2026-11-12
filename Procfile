release: DJANGO_SETTINGS_MODULE=snack_shop.settings_railway python manage.py migrate --noinput
web: DJANGO_SETTINGS_MODULE=snack_shop.settings_render python manage.py migrate --noinput && DJANGO_SETTINGS_MODULE=snack_shop.settings_render gunicorn snack_shop.wsgi:application --bind 0.0.0.0:$PORT
