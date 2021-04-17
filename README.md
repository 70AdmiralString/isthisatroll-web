# IsThisATroll? [![Build status](https://github.com/70AdmiralString/isthisatroll_web/actions/workflows/django.yml/badge.svg?branch=master)](https://github.com/70AdmiralString/isthisatroll_web/actions/workflows/django.yml?branch=master)

A website to spot trolls on Reddit using machine learning.

## Documentation

See the [wiki](https://github.com/70AdmiralString/isthisatroll_web/wiki).

## Usage

#### Dependencies

`Python3` is required to run the code, `pip` is used to install all required Python modules, so make sure you have both installed before proceeding further. If you are on a Debian-based system, you can install them with

    sudo apt install python3 python3-pip

We strongly suggest to run the app in a virtual environment. If you are not familiar with virtual environments, please see [this guide](https://docs.python.org/3/tutorial/venv.html).

#### Setup

Install Python dependencies:

    make install

Create the database:

    make migrate-db

Create a superuser for database admin:

    make superuser

Collect static files:

    make staticfiles

#### Linter and test

    make linter
    make test

#### Server startup

    make server
