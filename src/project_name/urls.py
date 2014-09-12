from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import SignInAndSignUp, LogoutView

urlpatterns = patterns(
    '',
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
