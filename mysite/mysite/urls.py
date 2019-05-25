from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('en_ka.urls')),
    path('en_ka/', include('en_ka.urls')),
    path('admin/', admin.site.urls),
]