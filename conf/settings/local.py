from .base import *

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/assets/'
STATIC_ROOT = BASE_DIR / 'assets'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

# Media files (Uploaded files)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
