from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #  post views
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog'))
]

'''
STOPPED AT PAGE 67

stuck on a error:

Using the URLconf defined in myblog.urls, Django tried these URL patterns, in this order:

admin/
The current path, blog, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.


'''