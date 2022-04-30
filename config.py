import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # variable for protecting against CSRF attack
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')

    # database variables for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # a bunch of variables for SMTP logging handler
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 25))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['l.misyuk@yandex.ru']
    
    # pagination variable
    POSTS_PER_PAGE = 5
