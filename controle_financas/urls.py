# controle_financas/urls.py
from django.contrib import admin
from django.urls import include, path
from financas.views import home, FaviconView, CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("financas/", include("financas.urls")),
    path("home/", home, name="home"),
    path("favicon.ico", FaviconView.as_view(), name="favicon"),
    ###### LOGIN ######
    path('', CustomLoginView.as_view()),
]
