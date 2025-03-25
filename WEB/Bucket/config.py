"""
Configuration settings for the Flask TV Show Episodes application.
"""

class Config:
    """Base configuration"""
    SECRET_KEY = 'your-secret-key-here'  # Replace with a secure key in production
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True

class ProductionConfig(Config):
    """Production configuration"""
    # Add production-specific settings here, like database URLs
    pass

# Configuration dictionary for easy access
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}