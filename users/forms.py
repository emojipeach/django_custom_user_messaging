from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    def clean_username(self):
        """ Ensures a unique username accounting for character case."""
        username = self.cleaned_data.get('username')
        lowercase_username = username.lower()
        if User.objects.filter(lowercase_username=lowercase_username):
            raise forms.ValidationError(_('A user with that username already exists.'))
        else:
            return username

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
