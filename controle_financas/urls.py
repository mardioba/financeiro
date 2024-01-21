# controle_financas/urls.py
from django.contrib import admin
from django.urls import include, path
from financas.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("financas/", include("financas.urls")),
    path("", home, name="home"),
]
