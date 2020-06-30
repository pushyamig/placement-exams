# standard libraries
import os
from typing import Any, Dict, List

# local libraries
from constants import ROOT_DIR


# Django settings

BASE_DIR: str = ROOT_DIR

CONFIG_DIR: str = os.path.join(BASE_DIR, os.getenv('ENV_DIR', os.path.join('config', 'secrets')))

DATABASES: Dict[str, Dict[str, str]] = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'placement_exams_local'),
        'USER': os.getenv('DB_USER', 'pe_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'pe_pw'),
        'HOST': os.getenv('DB_HOST', 'placement_exams_mysql'),
        'PORT': os.getenv('DB_PORT', '3306')
    }
}

FIXTURE_DIRS: List[str] = [
    CONFIG_DIR,
    os.path.join(BASE_DIR, 'test', 'fixtures')
]

LOGGING: Dict[str, Any] = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('LOG_LEVEL', 'INFO')
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'propagate': False
        },
    }
}

INSTALLED_APPS: List[str] = [
    'pe'
]

SECRET_KEY: str = os.getenv('SECRET_KEY', '-- A SECRET KEY --')

TIME_ZONE: str = os.getenv('TIME_ZONE', 'America/Detroit')
USE_TZ: bool = True