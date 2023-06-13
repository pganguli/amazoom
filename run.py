#!./bin/python

from app import create_app
from waitress import serve

if __name__ == "__main__":
    serve(create_app(), listen="*:8080")
