from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Username',
        })
        self.fields['password1'].widget = widgets.PasswordInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget = widgets.PasswordInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Verify password'
        })
