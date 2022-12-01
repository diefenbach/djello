from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("components_helper.urls")),
    path("", include("djello.urls")),
]
