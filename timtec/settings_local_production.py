# configurations for the production server
# https://docs.djangoproject.com/en/dev/ref/settings/
DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_ID = 2

ALLOWED_HOSTS = [
    'timtec.com.br',
    '.timtec.com.br',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timtec-production',
        'USER': 'timtec-production',
    }
}

MEDIA_ROOT = "/home/timtec-production/webfiles/media/"
STATIC_ROOT = "/home/timtec-production/webfiles/static/"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[timtec]'
DEFAULT_FROM_EMAIL = 'donotreply@m.timtec.com.br'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'WARN',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/timtec-production/django.log',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    # THIS FILE SETS PRODUCTION SPECIFIC
    # SENSITIVY VALUES (SUCH AS GOOGLE ANALYTICS KEY)
    from .settings_production import *
except ImportError:
    pass
