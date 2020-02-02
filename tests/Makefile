.PHONY: clean generate

all: clean generate test

clean: clean-django clean-dart
	rm -rf .coverage*

generate: dart_test_app django_test_app

test:
	./manage.py test test_middleware

clean-django:
	rm -rf django_test_app manage.py db.sqlite3 __pycache__

clean-dart:
	rm -rf dart_test_app

dart_test_app:
	mkdir dart_test_app
	cd dart_test_app && stagehand web-simple && pub get

django_test_app:
	django-admin startproject django_test_app .
	cp views.py urls.py django_test_app
	echo "\n# test app settings" >> django_test_app/settings.py
	echo "INSTALLED_APPS.insert(0, 'django_dart_webdev')" >> django_test_app/settings.py
	echo "MIDDLEWARE.insert(0, 'django_dart_webdev.middleware.ProxyMiddleware')" >> django_test_app/settings.py
	echo "DART_URL = '/dart/'" >> django_test_app/settings.py
	echo "WEBDEV_URL = 'http://127.0.0.1:8080'" >> django_test_app/settings.py
