from django.conf.urls import patterns, include, url
from django.contrib import admin
from profiles.views import SignInAndSignUp, LogoutView, AboutView

urlpatterns = patterns(
    '',
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', AboutView.as_view(),
        name='about'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
