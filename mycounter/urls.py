from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("counter/", include("counter.urls")),
    path('admin/', admin.site.urls),
]
