from .base import *
from .base import env


# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", True)

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='&m(!ehmav8z-qqi=)=fc2kp(^msd^3h@u=d0w*-7p659)%@h_k'
)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
HOST_URL = 'http://localhost:8000'

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': env.str("MYSQL_ENGINE", "django.db.backends.sqlite3"),
        'HOST': env.str('MYSQL_HOST'),
        'NAME': env.str('MYSQL_DB'),
        'USER': env.str('MYSQL_USER'),
        'PASSWORD': env.str('MYSQL_PASSWORD'),
        'PORT': env.int('MYSQL_PORT'),
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
