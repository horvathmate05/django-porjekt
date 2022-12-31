a  django -tól . contrib  import  admin
a  django -tól . URL -ek  importálási  útvonala , tartalmazza
#from django.conf.urls importálás tartalmazza: url

urlpatterns  = [
    elérési út ( 'admin/' , admin . site . urls ),
    elérési út ( r'' , include ( 'blog.urls' )),
    elérési út ( "accounts/" , include ( "django.contrib.auth.urls" )),   # new
]