from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%_7^n-7+drtbqnjb4^rj4we6#xnml784*9^td8ioqtg7m#!s1y'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

#ロギング設定
LOGING = {
    'version': 1, #1固定
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers': {
        #Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        #diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'blog': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },

    #ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },

        #フォーマッタの設定
        'formatters': {
            'dev': {
                'format': '\t'.join([
                    '%(asctime)s',
                    '[%(levelname)s]',
                    '%(pathname)s(Line:%(lineno)d)',
                    '%(message)s'
                ])
            },
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'





