from django.shortcuts import render, redirect
from .forms import PostForm, updateprofileinfo, updateprofileimage
from django.contrib.auth import authenticate
from .models import Post, updateInfo
from users.models import UserDetails
from django.contrib.auth.models import User
from django.core.paginator import Paginator


# Create your views here.
def userprofile(request):

    """ A view to return the users profile page """

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))

    data = Post.objects.all().order_by('date_posted').reverse()
    paginator = Paginator(data, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'userinfo': userinfo, 'data': data, 'page_obj': page_obj}
    return render(request, "profilepage/userprofile.html", context)


def update_info(request):

    """ A view to be able to change user info on the profile page """

    if request.method == 'POST':
        user = UserDetails.objects.get(user=User.objects.get(
            username=request.user.username))
        update_information = updateprofileinfo(request.POST, instance=user)

        if update_information.is_valid():

            profile = update_information.save(commit=False)

            profile.save()

            return redirect('userprofile')

    else:
        userinfo = UserDetails.objects.get(user=User.objects.get(
            username=request.user.username))
        update_information = updateprofileinfo(instance=userinfo)

    context = {'update_information': update_information}
    return render(request, "profilepage/update_info.html", context)


def update_image(request):

    """ A view to be able to change users image on the profile page """

    if request.method == 'POST':
        user = UserDetails.objects.get(user=User.objects.get(
            username=request.user.username))
        update_image = updateprofileimage(
            request.POST, request.FILES, instance=user)

        if update_image.is_valid():

            profile_picture = update_image.save(commit=False)

            profile_picture.save()

            return redirect('userprofile')

    else:
        userinfo = UserDetails.objects.get(user=User.objects.get(
            username=request.user.username))
        update_image = updateprofileimage(instance=userinfo)

    context = {'updateprofileimage': updateprofileimage}
    return render(request, "profilepage/update_image.html", context)


def newpost(request):

    """ A view to add a new blog post  """

    if request.method == 'POST':
        BlogPostForm = PostForm(request.POST)

        if BlogPostForm.is_valid():
            BlogPostForm.instance.user = request.user
            BlogPostForm.save(commit=True)
            return redirect('userprofile')

    else:
        BlogPostForm = PostForm()

    context = {'BlogPostForm': BlogPostForm}
    return render(request, 'profilepage/newpost.html', context)


def profile_list(request):

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))

    data = UserDetails.objects.all()
    paginator = Paginator(data, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'userinfo': userinfo, 'data': data, 'page_obj': page_obj}
    return render(request, 'profilepage/profile-list.html', context)
