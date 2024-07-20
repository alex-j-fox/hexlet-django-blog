install:
	poetry install

start:
	poetry run python manage.py runserver 0.0.0.0:8000

selfcheck:
	poetry check

lint:
	poetry run flake8 hexlet_django_blog

check: selfcheck lint
