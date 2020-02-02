install-tools:
	pub global activate stagehand
	pub global activate webdev
	pip install tox setuptools_scm

test:
	tox

clean:
	rm -rf build dist django_dart_webdev.egg-info .tox
	cd tests && make clean

release:
	python setup.py sdist bdist_wheel upload
