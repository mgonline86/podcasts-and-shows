import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# SQLALCHEMY_DATABASE_URI = 'postgresql://M&A:JiMmY1986$@localhost:5432/cgoss'
SQLALCHEMY_DATABASE_URI = 'postgres://glvjadjctjqmub:d55caded864121a60cd5c5ef833a30cf9d84bbc4f1c7766257a57bc92b56ac44@ec2-3-87-180-131.compute-1.amazonaws.com:5432/d84bpcfovr8ntt'
