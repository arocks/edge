from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline navbar-form pull-right'
        self.helper.form_id = 'signin-form'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Field('username', placeholder="Username", autofocus=""),
            Field('password', placeholder="Password"),
            Submit('sign_in', 'Sign in', css_class="btn-sm btn-success"),
            )


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signup-form'
        #self.helper.form_class = 'form-inline navbar-form pull-right'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        self.helper.help_text_inline = False
        self.helper.layout = Layout(
            Field('username', placeholder="Username"),
            Field('password1', placeholder="Password"),
            Field('password2', placeholder="Re-type Password"),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )
