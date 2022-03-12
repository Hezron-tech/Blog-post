
class Config:

    POST_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/quotes.json'

    POPULAR_QUOTE_API_URL='http://quotes.stormconsultancy.co.uk/popular.json'
    SINGLE_QUOTE_API_URL='http://quotes.stormconsultancy.co.uk/quotes/1.json'
    RANDOM_QUOTE_API_URL='http://quotes.stormconsultancy.co.uk/random.json'

   
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://hezron:hezzy@localhost/post'
   
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}