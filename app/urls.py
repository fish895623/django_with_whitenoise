from django.contrib import admin
from django.urls import path
from .views import current_datetime

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", current_datetime),
]
