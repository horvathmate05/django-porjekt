
import  os
 pathlib  importálási  útvonalból _

BASE_DIR  =  Elérési út ( __file__ ). megoldani (). szülő . szülő


SECRET_KEY  =  'django-insecure-1)0bl_!b!-6su79w+(%li0&8dbe3#@_9fgcn(1n&$oi#@%++-='

DEBUG  =  Igaz

ALLOWED_HOSTS  = [ '*' , '.pythonanywhere.com' , '127.0.0.1' , ]
CSRF_TRUSTED_ORIGINS  = [ 'https://*' , 'https://*.a.run.app' , 'https://*.127.0.0.1' ]


INSTALLED_APPS  = [
    'django.contrib.admin' ,
    'django.contrib.auth' ,
    'django.contrib.contenttypes' ,
    'django.contrib.sessions' ,
    'django.contrib.messages' ,
    'django.contrib.staticfiles' ,
    'oldal' ,
]

MIDDLEWARE  = ​​[
    'django.middleware.security.SecurityMiddleware' ,
    'django.contrib.sessions.middleware.SessionMiddleware' ,
    'django.middleware.common.CommonMiddleware' ,
    'django.middleware.csrf.CsrfViewMiddleware' ,
    'django.contrib.auth.middleware.AuthenticationMiddleware' ,
    'django.contrib.messages.middleware.MessageMiddleware' ,
    'django.middleware.clickjacking.XFrameOptionsMiddleware' ,
]

ROOT_URLCONF  =  'sajatwebhely.urls'

SABLONOK  = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates' ,
        'DIRS' : [],
        'APP_DIRS' : Igaz ,
        'OPCIÓK' : {
            'context_processors' : [
                'django.template.context_processors.debug' ,
                'django.template.context_processors.request' ,
                'django.contrib.auth.context_processors.auth' ,
                'django.contrib.messages.context_processors.messages' ,
            ],
        },
    },
]



ADATBÁZISOK  = {
    'alapértelmezett' : {
        'ENGINE' : 'django.db.backends.sqlite3' ,
        'NAME' : os . útvonalat . csatlakozás ( BASE_DIR  /  'db.sqlite3' ),
    }
}



AUTH_PASSWORD_VALIDATORS  = [
    {
        'NAME' : 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' ,
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.MinimumLengthValidator' ,
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.CommonPasswordValidator' ,
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.NumericPasswordValidator' ,
    },
]

LOGIN_REDIRECT_URL  =  "/"    # új
LOGOUT_REDIRECT_URL  =  "/"   # új


LANGUAGE_CODE  =  'hu-hu'

TIME_ZONE  =  'Európa/Budapest'

USE_I18N  =  Igaz

USE_L10N  =  Igaz

USE_TZ  =  Igaz


STATIC_URL  =  '/static/'
STATIC_ROOT  =  os . útvonalat . csatlakozás ( BASE_DIR , 'static' )


DEFAULT_AUTO_FIELD  =  'django.db.models.BigAutoField'