from django.conf.urls import patterns, include, url
from django.views import generic
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', generic.TemplateView.as_view(template_name='home.html'),
        name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
