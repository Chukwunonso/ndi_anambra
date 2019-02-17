# flake8: noqa
"""
Django settings for ndi_anambra project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import logging
from sys import path


import environ
env = environ.Env()

# Absolute filesystem path to the top-level project folder:

root = environ.Path(__file__) - 3
PROJECT_ROOT = root()

environ.Env.read_env(root('.env'))

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = root.path('ndi_anambra')

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Do not set SECRET_KEY or LDAP password or any other sensitive data here.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'taggit',
    'modelcluster',
    'dashboard',

    'wagtail.contrib.sitemaps',
    'wagtail.contrib.search_promotions',
    'wagtail.contrib.settings',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtailfontawesome',
    
    
    'utils',
    'pages',
    'blog',
    'events',
    'contact',
    'people',
    'photo_gallery',
    'products',
    'documents_gallery',

    'foundation_formtags',
    'wagtail_feeds',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'ndi_anambra.urls'

#Admins see https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Nonso Ibenegbu""", 'jollynony@yahoo.com'),
)

MANAGERS = ADMINS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'ndi_anambra.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///ndi_anambra'),
}

DATABASES['default']['ATOMIC_REQUESTS'] = True


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = root('static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


MEDIA_ROOT = root('media')
MEDIA_URL = '/media/'


# Django compressor settings
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE = False



# Google Maps Key

GOOGLE_MAPS_KEY = ''
DYNAMIC_MAP_URL = ''
STATIC_MAP_URL = ''

# Wagtail settings

LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "ndi_anambra"

WAGTAILSEARCH_RESULTS_TEMPLATE = 'utils/tags/search/search_results.html'

# Use Elasticsearch as the search backend for extra performance search results
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.search.backends.elasticsearch.ElasticSearch',
#         'INDEX': 'ndi_anambra',
#     },
# }

# Celery settings
# When you have multiple sites using the same Redis server,
# specify a different Redis DB. e.g. redis://localhost/5

BROKER_URL = 'redis://'

CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
)
