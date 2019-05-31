from django.contrib.staticfiles.urls import staticfiles_urlpatterns # NOTE: Not being used
from django.conf.urls import include # NOTE: Not being used
from django.contrib import admin # NOTE: Not being used
from django.urls import path
from . import views


urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
    path('<int:pk>/details/', views.details, name="details"),
]