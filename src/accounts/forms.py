from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools.forms import UserCreationForm, FriendlyPasswordResetForm
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-signin'
        self.helper.layout = Layout(
            Field('username', placeholder="Enter Email", autofocus=""),
            Field('password', placeholder="Enter Password"),
            HTML('<a href="{}">Forgot Password?</a>'.format(
                reverse("accounts:password-reset"))),
            Field('remember_me'),
            Submit('sign_in', 'Sign in',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        remember_me = self.cleaned_data.get('remember_me')
        if remember_me is True:
            ONE_MONTH = 30*24*60*60
            expiry = getattr(settings, "KEEP_LOGGED_DURATION", ONE_MONTH)
            self.request.session.set_expiry(expiry)


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-signin'
        self.helper.layout = Layout(
            Field('email', placeholder="Enter Email", autofocus=""),
            Field('name', placeholder="Enter Full Name"),
            Field('password1', placeholder="Enter Password"),
            Field('password2', placeholder="Re-enter Password"),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )


class PasswordChangeForm(authforms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('old_password', placeholder="Enter old password",
                  autofocus=""),
            Field('new_password1', placeholder="Enter new password"),
            Field('new_password2', placeholder="Enter new password (again)"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )


class PasswordResetForm(FriendlyPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email', placeholder="Enter email",
                  autofocus=""),
            Submit('pass_reset', 'Reset Password', css_class="btn-warning"),
            )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('new_password1', placeholder="Enter new password",
                  autofocus=""),
            Field('new_password2', placeholder="Enter new password (again)"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )
