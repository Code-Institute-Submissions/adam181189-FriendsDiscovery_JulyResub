from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserDetails



class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'email', 'first_name', 'last_name',
            'password1', 'password2']:
                self.fields[fieldname].help_text = None

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2']

        def clean_email(self):
        # Get the email
            email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
            try:
                match = User.objects.get(email=email)
            except User.DoesNotExist:
                # Unable to find a user, this is fine
                return email

            # A user was found with this as a username, raise an error.
            raise forms.ValidationError('This email address is already in use.')

    def signup(self, test, commit=True):

        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('gender', 'date_of_birth')


