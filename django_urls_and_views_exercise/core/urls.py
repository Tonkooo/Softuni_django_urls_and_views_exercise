from django.urls import path

from django_urls_and_views_exercise.core.views import index

urlpatterns = (
    path("", index),
    path("<int:pk>/", index),
    path("<slug:slug>/", index),
    path("<int:pk>/<slug:slug>/", index),
    path("<str:pk>/", index),

)