from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={
            'class': 'input-block-level',
            'placeholder': 'Username',
            })
        self.fields['password1'].widget = widgets.PasswordInput(attrs={
            'class': 'input-block-level',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget = widgets.PasswordInput(attrs={
            'class': 'input-block-level',
            'placeholder': 'Verify password'
        })
