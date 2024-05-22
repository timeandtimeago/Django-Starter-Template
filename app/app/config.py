import os

class AppConfig:
    SECRET_KEY = 'django-insecure-pl1a$a!kedhe9co&@gufi2#w30@8tgbqof0t!)v=$i#hi!^&c_'
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    LOCAL_DEV = True
    CORS_ALLOWED_ORIGINS = []
    PG_USER = 'django'
    PG_PASSWORD = 'db_password'
    PG_HOST = 'db'
    PG_PORT = '5432'
    PG_DB = 'postgres'

    # Static assets config values
    USE_GCS_STATIC_ASSETS = False
    GCS_STATIC_ASSETS_BUCKET = '<STATIC_ASSETS_BUCKET_NAME>'

    USE_STRUCTURED_LOGS = False

    DEFAULT_SUPERUSER_EMAIL='daniel@axon.consulting'
    DEFAULT_SUPERUSER_PASSWORD_SECRET_PATH=f"projects/<PROJECT_ID>/secrets/<PASSWORD_NAME>/versions/<VERSION>"
    DEFAULT_LOCAL_DEV_SUPERUSER_PASSWORD='password'

    
