from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    
    def unique_username(self):
        username = self.cleaned_data.get('username').lower()
        if User.objects.filter(lowercase_username=username):
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