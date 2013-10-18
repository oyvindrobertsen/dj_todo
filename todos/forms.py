from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.forms.fields import EmailField
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = EmailField(max_length=75)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

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
            'placeholder': 'Verify password',
        })
        self.fields['email'].widget = widgets.TextInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Email address',
        })

