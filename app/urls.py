from django.contrib import admin
from django.urls import path
from django.conf.urls import include

api_patterns = []

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]
