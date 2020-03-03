import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False

# USERNAME = os.getenv('FYYUR_USERNAME')
# PASSWORD = os.getenv('PASSWORD')
DATABASE_URL = os.getenv('DATABASE_URL')

# Enable debug mode.
# DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = f'postgres://{USERNAME}:{PASSWORD}@localhost:5432/fyyur-events'

SQLALCHEMY_DATABASE_URI = DATABASE_URL
