# Stores-API using SQLAlchemy

This is an API built with Flask, Flask-RESTful, Flask-JWT and Flask-SQLAlchemy.
Project based on Udemy course "[REST APIs with Flask and Python](https://www.udemy.com/rest-api-flask-and-python/)".


## Requirements
- Python3, install [here](https://www.python.org/downloads/)
- Virtual environments

## Setup
Install requirements
```
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Install using windows cmd
```
virtualenv --python=python3 .venv
".venv/Scripts/activate"
pip install -r requirements.txt
```

## Run
Make sure you are in the virtual environment and run
```
python app.py
```

### Database
Database is sqlite and will be stored in the db file.

### Deployment
Ready to be deployed on Heroku
