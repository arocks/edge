from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("me/", views.ShowProfile.as_view(), name="show_self"),
    path("<slug:slug>/", views.ShowProfile.as_view(), name="show_user"),
]
