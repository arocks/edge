from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    user_template_name = "users/home.html"
    anon_template_name = "anons/home.html"

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return self.user_template_name
        else:
            return self.anon_template_name
