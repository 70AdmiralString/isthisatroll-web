# Is this a troll?

A website to spot trolls on Reddit using machine learning.

## Documentation



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

#### Linter and test

    make linter
    make test

#### Server startup

    make server
