from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'full_name',
            'email',
            'branch',
            'semester',
            'bio',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Username'
            }),

            'full_name': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Full Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Email Address'
            }),

            'branch': forms.Select(attrs={
                'class': 'select select-bordered w-full'
            }),

            'semester': forms.NumberInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Semester'
            }),

            'bio': forms.Textarea(attrs={
                'class': 'textarea textarea-bordered w-full',
                'placeholder': 'Tell us about yourself...',
                'rows': 3
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Confirm Password'
        })
    )