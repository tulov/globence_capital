.. role:: shell(code)
   :language: shell

Тестовое задание от компании Globence Capital

Разработка
==========

Быстрые команды
---------------
* :shell:`make` Отобразить список доступных команд
* :shell:`make devenv` Создать и настроить виртуальное окружение для разработки
* :shell:`make lint` Проверить синтаксис и стиль кода с помощью `pylama`_
* :shell:`make clean` Удалить файлы, созданные модулем `distutils`_
* :shell:`make test` Запустить тесты
* :shell:`make sdist` Создать `source distribution`_

.. _pylama: https://github.com/klen/pylama
.. _distutils: https://docs.python.org/3/library/distutils.html
.. _source distribution: https://packaging.python.org/glossary/

Как подготовить окружение для разработки?
-----------------------------------------
.. code-block:: shell

    make devenv
    source venv/bin/activate
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Админка по адресу http://127.0.0.1:8000/
Документация по адресу: http://127.0.0.1:8000/api/v1/
