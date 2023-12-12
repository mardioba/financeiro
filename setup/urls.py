from app_fin.views import (
    FinListView,
    home,
    Total,
    FinDeleteView,
    FinUpdateView,
    movcad,
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fin/", FinListView.as_view(), name="fin_list"),
    path("", home, name="home"),
    path("total/", Total.as_view(), name="total"),
    path("delete/<int:pk>/", FinDeleteView.as_view(), name="fin_delete"),
    path("update/<int:pk>/", FinUpdateView.as_view(), name="fin_update"),
    path("movcad/", movcad, name="movcad"),
]
