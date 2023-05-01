import os
from pathlib import Path

import environ
import rest_framework.parsers
import rest_framework.permissions
from django.utils.translation import gettext_lazy as _

from core.jazzmin_conf import *  # noqa

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# READING ENV
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["*"]

# Application definition
DJANGO_APPS = [
    "modeltranslation",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

CUSTOM_APPS = [
    "apps.common",
    "apps.users",
    "apps.canban",
    "apps.social_auth",
]

THIRD_PARTY_APPS = [
    "jazzmin",
    "rest_framework",
    'rest_framework_simplejwt',
    "rest_framework.authtoken",
    "drf_yasg",
    "corsheaders",
    "captcha",
    "social_django",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
]

SITE_ID = 1

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.SessionAuthentication",
                                       "dj_rest_auth.jwt_auth.JWTCookieAuthentication",),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.FormParser', 'rest_framework.parsers.MultiPartParser'),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": env.str("DB_ENGINE"),
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.get_value("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/


MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')


def gettext(s):
    return s


LANGUAGES = (
    ("en", gettext("English")),
    ("ru", gettext("Русский")),
    ("uz", gettext("O'zbekcha")),
)
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{env.str('REDIS_URL', 'redis://localhost:6379/0')}",
        "KEY_PREFIX": "boilerplate",
    }
}

# CELERY CONFIGURATION
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://localhost:6379")
CELERY_RESULT_BACKEND = env.str("CELERY_BROKER_URL", "redis://localhost:6379")

CELERY_TIMEZONE = "Asia/Tashkent"

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')

SOCIAL_AUTH_JSONFIELD_ENABLED = True

# SOCIAL AUTH CONFIGURATION
SOCIALACCOUNT_PROVIDERS = {  # noqa
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    #     "apple": {
    #         "APP": {
    #             # Your service identifier.
    #             "client_id": env.str("SOCIALACCOUNT_APPLE_CLIENT_ID", "org.uicgroup.ayoluchun"),
    #             # The Key ID (visible in the "View Key Details" page).
    #             "secret": env.str("SOCIALACCOUNT_APPLE_SECRET", "6DP9RD92NY"),
    #             # Member ID/App ID Prefix -- you can find it below your name
    #             # at the top right corner of the page, or it’s your App ID
    #             # Prefix in your App ID.
    #             "key": env.str("SOCIALACCOUNT_APPLE_TEAM_ID", "KHGXWF53U9"),  # team id
    #             # The certificate you downloaded when generating the key.
    #             "certificate_key": """-----BEGIN PRIVATE KEY-----
    # MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgL3oIve1fiKQJx0gl
    # SLQkQG8zyhwhMbg/TSajVdVuURigCgYIKoZIzj0DAQehRANCAASplpoy6+148IwB
    # CZahdME/LeHIziIHGTNIZQOAIRYdNQNugfiYZI9RnV/07wK0bYb8hWB65TXz5Kek
    # szdGoZ+F
    # -----END PRIVATE KEY-----""",
    #         }
    #     },
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env.str("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", "")  # noqa
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env.str("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", "")  # noqa

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

OAUTH_CALLBACK_URL = f"{env.str('HOST', '')}"

REST_USE_JWT = True
