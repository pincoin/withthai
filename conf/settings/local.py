from django.utils.translation import ugettext_lazy as _

from .base import *

# Internationalization

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('ko', _('Korean')),
    ('th', _('Thai')),
    ('en', _('English')),
    ('ja', _('Japanese')),
    ('zh', _('Chinese')),
]
LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

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

# Email reports

ADMINS = [('devops', 'dev@withthai.com'), ]

# Media files (Uploaded files)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Dummy Cache for development

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'TIMEOUT': 300,
        'TIMEOUT_HOUR': 3600,
        'TIMEOUT_DAY': 86400,
    }
}
