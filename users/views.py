from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import SignupForm, UserProfileForm

# https://www.youtube.com/watch?v=Tja4I_rgspI 
# (Followed this tutorial to make a custom signup sheet work)

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'

    context = {'username': username}
    return render(request, 'home/templates/home/index.html', context)


@login_required
def profile(request):
    return render(request, "profilepage/blog.html")


def extendedSignup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('account_login')
    else:
        form = SignupForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'account/signup.html', context)
