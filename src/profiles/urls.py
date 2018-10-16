from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('me/', views.ShowProfile.as_view(), name='show_self'),
    path('me/edit/', views.EditProfile.as_view(), name='edit_self'),
    path('<slug:slug>/', views.ShowProfile.as_view(),
         name='show'),
]
