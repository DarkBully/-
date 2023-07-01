from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your password'
            }
        )
    )

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your firstname'
            }
        )
    )
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your lastname'
            }
        )
    )
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your username'
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your email'
            }
        )
    )
    
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your password'
            }
        )
    )
    password1 = forms.CharField(
        label='Password Repeat',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Input your password'
            }
        )
    )