import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta
import dj_database_url

# Load Environment Variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '172.17.0.1', 'localhost', 'one-team-stat.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Applications
    'core.apps.CoreConfig',
    'gamecore.apps.GamecoreConfig',
    'games.apps.GamesConfig',
    'gamestat.apps.GamestatConfig',
    'corsheaders',
    
    # Third party frameworks
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist'
]

MIDDLEWARE = [

    # Custom middleware for cookie authentication
    'core.middleware.CookieJWTAuthMiddleware',
    
    # Djago Middlewares
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
]

ROOT_URLCONF = 'OneTeamStat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OneTeamStat.wsgi.application'


REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [      
            # Custom django restframework-simple JWT Cookie based authentication
            'core.authentication.CustomCookieJWTAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],

        'DEFAULT_FILTER_BACKENDS': [
            'rest_framework.filters.SearchFilter',
        ],
        
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',
            'rest_framework.parsers.FormParser', 
            'rest_framework.parsers.MultiPartParser', 
        ]
        }

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    
    "SIGNING_KEY": os.getenv('DJANGO_SECRET_KEY'),
    "VERIFYING_KEY": None,

    "CSRF_COOKIE_SECURE": False,
    "CSRF_COOKIE_HTTPONLY":  False,
    "SESSION_COOKIE_SECURE":  False,
    
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_COOKIE": "access_token",
    "AUTH_COOKIE_REFRESH" : "refresh_token",
    "AUTH_COOKIE_SECURE": True,
    "AUTH_COOKIE_PATH": "/",
    "AUTH_COOKIE_SAMESITE": "",
    "AUTH_COOKIE_HTTP_ONLY": True,

    # Custom Token Claim which adds username, email and role
    "TOKEN_OBTAIN_SERIALIZER": "core.CustomTokenClaim.MyTokenObtainPairSerializer",
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.getenv('PGNAME'),
    #     'USER' : os.getenv('PGUSER'),
    #     'PASSWORD' : os.getenv('PGPASSWORD'),
    #     'HOST' : os.getenv('PGHOST'),
    #     'PORT' : os.getenv('PGPORT', '5432')
    # }

    # Render database
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'core.MyUser'

