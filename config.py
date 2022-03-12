import os
import re

class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://hezron:hezzy@localhost/post'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # # simple mde  configurations
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


# class Config:

    
#     RANDOM_QUOTE_API_URL='http://quotes.stormconsultancy.co.uk/random.json'

   
#     SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://hezron:hezzy@localhost/post'
   
    


# class ProdConfig(Config):
#     pass


# class DevConfig(Config):
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }