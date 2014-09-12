from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.SignInAndSignUp.as_view(), name="home", ),
)
