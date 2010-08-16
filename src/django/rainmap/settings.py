# Configuration file for Rainmap
# Please read through this file and edit the appropriate sections (DATABASE,
# EMAIL_ and SECRET_KEY *at least*)
# When finished, rename this file to settings.py for Django to find it

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('alexandru', 'alex@hackd.net'),
)

import os.path
PROJECT_DIR = os.path.dirname(__file__)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2',
        'NAME': 'rainmap_db',
        'USER': 'rainmapdba',
        'PASSWORD': 'k32iNKHY6QGt9ERMFj4T',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False # we don't have any other languages right now

# Date and time localization
USE_L10N = True

# Absolute path to the directory that will store scan results.
OUTPUT_ROOT = "/var/local/rainmap/storage/"

# URL prefix for the location that stores the scan results. Make sure to use a
# trailing slash
OUTPUT_URL = "/storage/"

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = "/var/local/rainmap/public/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

ALLOWED_INCLUDE_ROOTS = MEDIA_ROOT

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'Xm@kRw3VSjIUxP{,NfZh8WrOpl:%FEuqv6Lo<a1=Gs9_^-TicM'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INTERNAL_IPS = ('127.0.0.1', )

ROOT_URLCONF = 'rainmap.urls'


TEMPLATE_DIRS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, "templates/default"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'djcelery',
    'registration',
    'rainmap.core',
)

AUTH_PROFILE_MODULE = 'core.UserProfile'

### REGISTRATION ###
REGISTRATION_OPEN = True # can new accounts be registered?
ACCOUNT_ACTIVATION_DAYS = 7 # how long before an acct can be activated
LOGIN_REDIRECT_URL = '/'

### EMAIL SERVER ###
EMAIL_SUBJECT_PREFIX = '[rainmap]'
EMAIL_HOST = 'mail.hackd.net' # smtp server
EMAIL_HOST_USER = 'replay@labs.hackd.net'
EMAIL_HOST_PASSWORD = "2)i40a%6'o+U_7I"
EMAIL_PORT = 587
# Email for registrations
DEFAULT_FROM_EMAIL = 'replay@labs.hackd.net'
# Email address used as sender by celeryd for error mail
SERVER_EMAIL = "replay@labs.hackd.net"

### RABBITMQ ###
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "rainq"
BROKER_PASSWORD = "64)0~D#7]5}vdAu"
BROKER_VHOST = "li155-5"

CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("core.tasks", )
