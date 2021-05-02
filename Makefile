SHELL := /bin/bash
PYTHON ?= python
PIP ?= pip
PYCODESTYLE ?= $(PYTHON) -m pycodestyle
FLAKE8 ?= $(PYTHON) -m flake8
PYLINT ?= $(PYTHON) -m pylint
NOINPUT_OPT := $(shell if [ "$$NOINPUT" = true ]; then echo "--noinput"; fi)

SRC_FILES := $(shell find . -name "*.py" -not -path "*/migrations/*")

ISTHISATROLL_ENV := development

default:
	@echo "Choose a target"

install:
	@$(PIP) install -r requirements.txt

linter:
	@echo "=== Pycodestyle ==="
	@$(PYCODESTYLE) --max-line-length=100 $(SRC_FILES)
	@echo "=== Flake8 ==="
	@$(FLAKE8) --max-line-length=100 --ignore=F401 $(SRC_FILES)
	@echo "=== Done ==="

test:
	@$(PYTHON) -Wall manage.py test

delete-db:
	@rm -f db.sqlite3

migrate-db:
	$(PYTHON) manage.py makemigrations $(NOINPUT_OPT)
	$(PYTHON) manage.py migrate $(NOINPUT_OPT)

server:
	$(PYTHON) manage.py runserver

production-server:
	@ISTHISATROLL_ENV=production $(PYTHON) manage.py collectstatic
	@ISTHISATROLL_ENV=production gunicorn isthisatroll.wsgi

superuser:
	$(PYTHON) manage.py createsuperuser
