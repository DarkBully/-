from django import forms

from .models import Post


class UserPageForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'description']
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control form-control-lg',
                }
            ),
            'description' : forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                }
            )
        }