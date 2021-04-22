from django import forms
from .models import addPost


class PostForm(forms.ModelForm):
    class Meta:
        model = addPost
        fields = ('new_post',)
