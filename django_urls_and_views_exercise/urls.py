"""
URL configuration for django_urls_and_views_exercise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_urls_and_views_exercise.departments.views import department_2_details, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('django_urls_and_views_exercise.core.urls')),
    path("departments/", include('django_urls_and_views_exercise.departments.urls')),
    # path("employees/", include([
    #     path("asd/", index),
    #     path("asd2/", department_2_details)
    # ]))
]
