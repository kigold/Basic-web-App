import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret key'

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/databaseName'
#SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = '"Sender"'

# Flask-User settings
USER_APP_NAME = ""

# oauth setting
