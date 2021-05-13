from django import forms
from .models import Post
from users.models import UserDetails
from django.contrib.auth.models import User


# Add a new blog post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('new_post',)


# form for changing personal details on the profile page
class updateprofileinfo(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('gender', 'date_of_birth', 'bio', 'nationality')


# form for changing the image on the profile page
class updateprofileimage(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('profile_pic',)


# form for adding a heart to the user

class addheartForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ("received_hearts",)
