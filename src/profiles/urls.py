from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^me/delete$', views.DeleteProfile.as_view(), name='delete_self'),
    url(r'^(?P<username>\w+)$', views.ShowProfile.as_view(),
        name='show'),
)
