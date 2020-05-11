class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = "611b8ca39a9a44b28ab62a58315fb11d"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@database:5432/db_dev"
