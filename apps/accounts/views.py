# from django.shortcuts import render
from django.views import generic
from . import forms
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages


class SignInAndSignUp(generic.edit.FormMixin, generic.TemplateView):

    signin_form_class = forms.LoginForm
    signup_form_class = forms.SignupForm

    def get(self, request, *args, **kwargs):
        if "signin_form" not in kwargs:
            kwargs["signin_form"] = self.signin_form_class()
        if "signup_form" not in kwargs:
            kwargs["signup_form"] = self.signup_form_class()
        return super(SignInAndSignUp, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'sign_in' in request.POST:
            form = self.signin_form_class(**self.get_form_kwargs())
            if not form.is_valid():
                messages.add_message(request,
                                     messages.ERROR,
                                     "Unable login! "
                                     "Check username/password")
                return super(SignInAndSignUp, self).get(request,
                                   signup_form=self.signup_form_class(),
                                   signin_form=form)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(self.request, user)
            else:
                messages.add_message(request, messages.ERROR,
                                     "Unable to find given username!")
        if 'sign_up' in request.POST:
            form = self.signup_form_class(**self.get_form_kwargs())
            if not form.is_valid():
                messages.add_message(request,
                                     messages.ERROR,
                                     "Unable to register! "
                                     "Please retype the details")
                return super(SignInAndSignUp, self).get(request,
                                   signin_form=self.signin_form_class(),
                                   signup_form=form)
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            messages.add_message(request,
                                 messages.INFO,
                                 "{0} added sucessfully".format(
                                     username))
            # Login automatically
            user = authenticate(username=username, password=password)
            login(self.request, user)
        return redirect("home")


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.INFO,
                             "Logout successful!")
        return super(LogoutView, self).get(request, *args, **kwargs)


class AboutView(generic.TemplateView):
    template_name = "about.html"
