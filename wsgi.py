"""
WSGI konfiguráció a djangogirls projekthez.
A hívható WSGI-t ``application`` nevű modulszintű változóként teszi közzé.
A fájlról további információkért lásd:
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import  os

a  django -tól . mag . wsgi  import  get_wsgi_application

os . környezetében . setdefault ( "DJANGO_SETTINGS_MODULE" , "djangogirls.settings" )

application  =  get_wsgi_application ()