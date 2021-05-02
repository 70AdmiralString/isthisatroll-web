# IsThisATroll? [![Build status](https://github.com/70AdmiralString/isthisatroll_web/actions/workflows/django.yml/badge.svg?branch=master)](https://github.com/70AdmiralString/isthisatroll_web/actions/workflows/django.yml?branch=master)

A website to spot trolls on Reddit using machine learning.

## Project rules

Please see the [wiki](https://github.com/70AdmiralString/isthisatroll_web/wiki).

## Usage

#### Dependencies

`Python3` is required to run the code, `pip` is used to install all required Python modules, so make sure you have both installed before proceeding further. If you are on a Debian-based system, you can install them with

    sudo apt install python3 python3-pip

Running the app in a virtual environment is strongly suggested. If you are not familiar with virtual environments, please see [this guide](https://docs.python.org/3/tutorial/venv.html).

#### Setup

Install Python dependencies:

    make install

Create the database:

    make migrate-db

Create a superuser for database admin:

    make superuser

#### Test and linter

Always make sure that the code is passing all basic consistency tests:

    make test

It's also a good practice to respect some basic Python coding rules. You can check them with

    make linter

#### Server startup

During development, you should generally run the server in development mode. To start the server in development mode use

    make server

This launches an instance of the built-in Django development server.

In the rare cases in which you have to test the production server, you can run a mock instance of it with

    make production-server

This collects all static files and launches an instance of `gunicorn`.

**Note:** the mock production server still uses the `SQLite` development database and not the `PostgreSQL` production database.

#### Deployment

The `ISTHISATROLL_ENV` environment variable is used to decide whether to run the server in production mode or in development mode. When deploying the server it should be set to `production`.
