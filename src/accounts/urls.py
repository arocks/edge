from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
)
