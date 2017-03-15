import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    COMPRESSOR_OUTPUT_DIR = '%s/app/static/dist' % sys.path[0]
    COMPRESSOR_STATIC_PREFIX = '/static/dist'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    COMPRESSOR_DEBUG = True


class ProductionConfig(Config):
    COMPRESSOR_DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
