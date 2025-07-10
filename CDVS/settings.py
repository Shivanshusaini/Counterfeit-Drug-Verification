# from pathlib import Path
# import os
# import dj_database_url
# from dotenv import load_dotenv

# # ✅ .env file ko load karo
# load_dotenv()

# # 📁 Base directory
# BASE_DIR = Path(__file__).resolve().parent.parent

# # 📸 Media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SECRET_KEY = os.getenv('SECRET_KEY')

# DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
# # ✅ Installed Apps
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'verification',
# ]

# # ✅ Middleware
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ whitenoise pehle aaye security ke baad
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'CDVS.urls'

# # ✅ Templates
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'template')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'CDVS.wsgi.application'

# # # ✅ Automatic DB config: LOCAL = SQLite, PROD = Postgres
# # DATABASES = {
# #     'default': dj_database_url.config(
# #         default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
# #     )
# # }
# DATABASE_URL = os.getenv('DATABASE_URL')

# if DATABASE_URL:
#     # Production: Postgres on Render
#     DATABASES = {
#         'default': dj_database_url.parse(DATABASE_URL)
#     }
# else:
#     # Local: SQLite fallback
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }


# # ✅ Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # ✅ Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # ✅ Static files
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # ✅ Collectstatic ke liye
# os.environ['DJANGO_COLLECTSTATIC'] = '1'

# # ✅ Default primary key
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# ✅ .env file ko load karo
load_dotenv()

# 📁 Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Secret & Debug
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# ✅ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'verification',
    'storages',  # ✅ Add storages for Supabase/S3
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CDVS.urls'

# ✅ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CDVS.wsgi.application'

# ✅ Automatic DB config
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ✅ Supabase Storage: Use S3 backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('SUPABASE_KEY')  # Supabase service role key
AWS_SECRET_ACCESS_KEY = os.getenv('SUPABASE_SECRET', '')  # Optional for Supabase
AWS_STORAGE_BUCKET_NAME = os.getenv('SUPABASE_BUCKET')  # e.g. 'qr-codes'
AWS_S3_ENDPOINT_URL = os.getenv('SUPABASE_URL')  # e.g. https://xxxx.supabase.co/storage/v1
AWS_S3_REGION_NAME = None
AWS_S3_ADDRESSING_STYLE = "path"
AWS_S3_SIGNATURE_VERSION = "s3v4"

# ✅ Media URL
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/object/public/{AWS_STORAGE_BUCKET_NAME}/"

# ✅ Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Collectstatic ke liye
os.environ['DJANGO_COLLECTSTATIC'] = '1'

# ✅ Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
