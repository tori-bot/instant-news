import os

class Config:
    #generate configuraion parent class
    API_BASE_URL='https://newsapi.org/v2/sources?language=en&apiKey={}'
    API_KEY=os.environ.get('API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    #production configuration child
    pass

class DevConfig(Config):
    #development configuration child
DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
