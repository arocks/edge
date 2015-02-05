from accounts.views import SignInAndSignUp
from django.views import generic


class HomePage(SignInAndSignUp):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
