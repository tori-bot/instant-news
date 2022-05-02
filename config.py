import os

class Config:
    #generate configuraion parent class
    API_BASE_URL='https://newsapi.org/v2/everything?q=Kenya&sortBy=popularity&apiKey={}'
    API_KEY=os.environ.get('API_KEY')

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
