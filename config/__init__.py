class Config():
    SECRET_KEY = '1234'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///servertree.db'
    JSON_SORT_KEYS = False