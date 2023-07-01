from django import forms

from .models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg'
                }
            ),
            'post': forms.NumberInput(
                attrs={
                    'type': 'hidden'
                }
            )
        }
        labels = {
            'content': 'Comment',
            'post': ''
        }