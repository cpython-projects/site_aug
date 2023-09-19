from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'id': 'username',
                                                                               'placeholder': 'Your Username',
                                                                               'data-rule': 'minlen:4',
                                                                               'data-msg': 'Please enter at least 4 chars'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'id': 'password1',
                                                                                    'placeholder': 'Input password',
                                                                                    'data-rule': 'minlen:4',
                                                                                    'data-msg': 'Please enter at least 4 chars'}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'id': 'username',
                                                                       'placeholder': 'Your Username',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                           'id': 'email',
                                                                           'data-rule': 'email',
                                                                           'data-msg': 'Please enter a valid email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                               'id': 'password1',
                                                                               'placeholder': 'Input password',
                                                                               'data-rule': 'minlen:4',
                                                                               'data-msg': 'Please enter at least 4 chars'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'id': 'password2',
                                                                                    'placeholder': 'Repeat password',
                                                                                    'data-rule': 'minlen:4',
                                                                                    'data-msg': 'Please enter at least 4 chars'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


