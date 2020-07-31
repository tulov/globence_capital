all:
	@echo "make devenv		- Create & setup development virtual environment"
	@echo "make lint		- Check code with pylama"
	@echo "make clean		- Remove files created by distutils"
	@echo "make sdist		- Make source distribution"
	@exit 0

clean:
	rm -fr *.egg-info dist

devenv: clean
	rm -rf venv
	# создаем новое окружение и устанавливаем основные + dev зависимости
	# из extras_require (см. setup.py)
	python3.8 -m venv venv
	venv/bin/pip install -Ue '.[dev]'

lint:
	venv/bin/pylama

sdist: clean
	# официальный способ дистрибуции python-модулей
	python3 setup.py sdist
