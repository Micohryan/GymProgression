from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepg, name="homepg"),
    path('insert', views.create_workout, name = "create_workout"),
]