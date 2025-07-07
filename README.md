# Counterfeit-Drug-Verification## 🌐 Django + Render Deploy Steps (Production Ready)

1️⃣ **Settings.py में updates**
```py
# Production के लिए जरूरी:
DEBUG = False  
ALLOWED_HOSTS = ['your-render-url.onrender.com']

# WhiteNoise सबसे ऊपर:
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  ...
]

# Static files setup:
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Render पर build time input error से बचने के लिए:
import os
os.environ['DJANGO_COLLECTSTATIC'] = '1'
2️⃣ Render Deploy settings

✅ Build Command:


pip install -r requirements.txt && python manage.py collectstatic --noinput

✅ Start Command:

gunicorn CDVS.wsgi

3️⃣ Static Folder

अपनी CSS / JS files static/ folder में रखो।

Local में check करने के लिए:

python manage.py collectstatic

4️⃣ Final Checks

Git में commit करके push करो:

git add .
git commit -m "Deploy ready"
git push origin main
Render पर Redeploy करो।

