import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
        Set Config variables for the flask application.
        Using Environment variables where available otherwise
        create the config variable if not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
        #communicating to our database either with the database URL or if we can't find that create sqlite file that will server as our development database
        #either way we'll be able to find a database no problem
    SQLALCHEMY_TRACK_MODIFICATIONS = False
        #Turn off update messages from sqlalchemy
        #trying to not get overloaded with info eery time we make a new change to database
        #else it will continue to say "you've made a change here"

    