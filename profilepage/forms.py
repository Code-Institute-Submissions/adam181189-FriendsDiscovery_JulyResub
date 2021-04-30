from django import forms
from .models import Post
from users.models import UserDetails


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('new_post',)


class updateprofileinfo(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('gender', 'date_of_birth', 'bio', 'nationality')
