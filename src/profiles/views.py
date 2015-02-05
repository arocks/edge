from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from braces.views import LoginRequiredMixin
from . import forms


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        username = self.kwargs.get('username')
        if username:
            user = get_object_or_404(User, username=username)
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        # kwargs["user_form"] = forms.UserForm(instance=user)
        # kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super().get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.add_message(request,
                                 messages.ERROR,
                                 "There was a problem with the form",
                                 "Please check the entered details")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super().get(request,
                               user_form=user_form,
                               profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.add_message(request,
                             messages.INFO,
                             "Profile details saved!")
        return redirect("profiles:show_self")


class DeleteProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/delete_profile.html"
    http_method_names = ['get', 'post']

    def post(self, request, *args, **kwargs):
        user = self.request.user
        username = user.username
        logout(request)
        user.delete()
        messages.add_message(request, messages.WARNING,
                             "Deleted User: {}!".format(username))
        return redirect("home")
