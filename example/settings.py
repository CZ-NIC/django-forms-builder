import os


DEBUG = True
SITE_ID = 1
EXAMPLE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = EXAMPLE_ROOT.split(os.sep)[-1]
STATIC_URL = "/static/"
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
SECRET_KEY = "asdfa4wtW#$Gse4aGdfs"

if 'TOX_WORK_DIR' in os.environ:
    DATABASE_FILEPATH = os.path.join(os.environ['TOX_WORK_DIR'], 'tests.db')
else:
    DATABASE_FILEPATH = os.path.join(EXAMPLE_ROOT, 'dev.db')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_FILEPATH,
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(EXAMPLE_ROOT, "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'forms_builder.forms',
)

FORMS_BUILDER_EXTRA_FIELDS = (
    (100, "django.forms.BooleanField", "My cool checkbox"),
)

TEMPLATE_DEBUG = DEBUG

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
