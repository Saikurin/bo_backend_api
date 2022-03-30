# Back-Office of a resale point for Thibault's Boat products

Project created as part of my graduate training at CFA INSTA.

The API was developed with Django Rest Framework 3.13.1 and Django 4.0.3.

Its purpose is to provide the front-end application with data on products and their sales history.

## Prerequisites

- [Pyenv](https://github.com/pyenv/pyenv) with Python (3.6, 3.7, 3.8, 3.9, 3.10)

## Setup
- `python3 -m venv env`
- `source env/bin/activate`
- `python3 -m pip install --upgrade pip`
- `pip install -r requirements.txt`

## Running API
- `python manage.py migrate` # Execute the migrations in order to have the database up to date
- `python manage.py loaddata api/fixtures/*.json` # Load the initial data into the database
- `python manage.py runserver` # Run the API server
