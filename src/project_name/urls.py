from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from . import views
import users.urls

# Personalized admin site settings like title and header
admin.site.site_title = "{{ project_name|capfirst }} Site Admin"
admin.site.site_header = "{{ project_name|capfirst }} Administration"


urlpatterns = [
    path("", views.HomePageView.as_view(), name="site_home"),
    path("accounts/", include("allauth.urls")),
    path("users/", include(users.urls)),
    path("admin/", admin.site.urls),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
