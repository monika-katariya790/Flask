import os 

class Config:
    SECRET_KEY = '5f874872fc63986b225167f28d294a72'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =  os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =  os.environ.get('EMAIL_PASSWORD')