class Config(object):

    #Secret key
    SECRET_KEY = 'my_very_secret_key'

    ITEMS_PER_PAGE = 25

    SQLALCHEMY_BINDS = {
        # 'mysql_bind': 'mysql+mysqlconnector://localhost:3306/tmpdb',
        'sample_bind': 'sqlite:///sample.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False