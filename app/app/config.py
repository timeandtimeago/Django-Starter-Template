import os

class AppConfig:
    SECRET_KEY = 'django-insecure-pl1a$a!kedhe9co&@gufi2#w30@8tgbqof0t!)v=$i#hi!^&c_'
    DEBUG = True
    ALLOWED_HOSTS = []
    LOCAL_DEV = True
    CORS_ALLOWED_ORIGINS = []
    PG_USER = 'django'
    PG_PASSWORD = 'db_password'
    PG_HOST = 'localhost'
    PG_PORT = '5432'
    PG_DB = 'postgres'

    # Static assets config values
    USE_GCS_STATIC_ASSETS = False
    GCS_STATIC_ASSETS_BUCKET = ''
    
