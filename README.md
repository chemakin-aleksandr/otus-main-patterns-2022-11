# Групповое ДЗ курса "Архитектура и шаблоны проектирования". Группа 2022-11-Python

Требуется python 3.10. Виртуальное окружение должно быть предварительно установлено и активировано.
Управление зависимостями выполняется через [pip-tools](https://github.com/jazzband/pip-tools). Зависимости указаны в [pyproject.toml](https://github.com/jazzband/pip-tools#requirements-from-pyprojecttoml).

Установка зависимостей:

```bash
pip install --upgrade pip pip-tools
make
```

Запуск линтера:

```bash
# run lint
make lint
```

Запуск тестов:

```bash
# run unit tests
make test
```
