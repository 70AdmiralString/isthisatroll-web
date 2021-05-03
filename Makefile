# --- Configuration ---

SHELL := /bin/bash
PYTHON ?= python
PIP ?= pip
PYCODESTYLE ?= $(PYTHON) -m pycodestyle
FLAKE8 ?= $(PYTHON) -m flake8
PYDOCSTYLE ?= $(PYTHON) -m pydocstyle
NOINPUT_OPT := $(shell if [ "$$NOINPUT" = true ]; then echo "--noinput"; fi)

SRC_FILES := $(shell find . -name "*.py" -not -path "*/migrations/*")

# Setting the default server to development
ISTHISATROLL_ENV := development


# --- Messages ---

# Announcement message
define ANNOUNCE_BODY

-------------------
|  IsThisATroll?  |
-------------------

A website to spot trolls on Reddit using machine learning.

---

endef
export ANNOUNCE_BODY

# Quick help message
define QUICK_HELP
Choose a target:

  - install               install dependencies
  - migrate-db            create and update database structure
  - delete-db             delete the development database
  - superuser             create a superuser for database admin
  - test                  run unit tests
  - linter                run code linters
  - server                run the development server
  - production-server     run a mock production server
  - help                  show an expanded help message (README.md)

endef
export QUICK_HELP


# --- Rules ---

default:
	@echo "$$ANNOUNCE_BODY"
	@echo "$$QUICK_HELP"

install:
	@$(PIP) install -r requirements.txt

linter:
	@echo "=== Code consistency and style ==="
	@echo "- Pycodestyle"
	@$(PYCODESTYLE) --max-line-length=100 $(SRC_FILES)
	@echo "- Flake8"
	@$(FLAKE8) --max-line-length=100 --ignore=F401 $(SRC_FILES)
	@echo "=== Docstrings style ==="
	@echo "- Pydocstyle"
	@$(PYDOCSTYLE) --ignore=D100,D101,D104,D203,D212
	@echo "=== Done ==="

test:
	@$(PYTHON) -Wall manage.py test

delete-db:
	@rm -f db.sqlite3

migrate-db:
	@$(PYTHON) manage.py makemigrations $(NOINPUT_OPT)
	@$(PYTHON) manage.py migrate $(NOINPUT_OPT)

server:
	@echo "$$ANNOUNCE_BODY"
	@echo "Starting development server..."
	@$(PYTHON) manage.py runserver

production-server:
	@echo "$$ANNOUNCE_BODY"
	@echo "Starting mock production server..."
	@ISTHISATROLL_ENV=production $(PYTHON) manage.py collectstatic
	@ISTHISATROLL_ENV=production gunicorn isthisatroll.wsgi

superuser:
	@$(PYTHON) manage.py createsuperuser

help:
	@less README.md
