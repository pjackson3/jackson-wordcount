"""The configurations for the app."""

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    """The base config."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sdjf;lajdsflkjdsf;ljsda'
                                'flkjsdaf;l ljfoiwej8r2-4578qewupocmv?Z'
                                'n/lkhoqytr9807509')


class ProductionConfig(Config):
    """The production config for the app."""

    DEBUG = False


class StagingConfig(Config):
    """The configuration for the staging environment."""

    DEBUG = True


class DevelopmentConfig(Config):
    """The configuration for development."""

    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """The configuration for testing."""

    TESTING = True
