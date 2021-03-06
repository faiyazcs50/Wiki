from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:name>', views.Entry, name="visit"),
    path('random/', views.random_selector, name="random_selector")
]
