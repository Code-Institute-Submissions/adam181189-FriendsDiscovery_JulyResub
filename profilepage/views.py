from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, updateprofileinfo, updateprofileimage, addheartForm
from django.contrib.auth import authenticate
from .models import Post, updateInfo
from users.models import UserDetails
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import DetailView
from friendship.models import Friend, Follow, Block, FriendshipRequest
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import template
import datetime

try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User


def get_friendship_context_object_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_NAME", "user")


def get_friendship_context_object_list_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME", "users")


# Create your views here.
def userprofile(request):
    """ A view to return the users profile page """

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))

    user = get_object_or_404(user_model, username=request.user.username)

    friends = Friend.objects.friends(user)

    data = []
    for post in Post.objects.all().order_by('date_posted').reverse():
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(post.user)
        print(request.user.username)
        print(str(post.user) == str(request.user.username))
        if post.user in friends or str(post.user) == str(request.user.username):
            data.append(post)

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
    """ A view to return a list of all user profile pages """

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))

    data = UserDetails.objects.all()
    paginator = Paginator(data, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'userinfo': userinfo, 'data': data, 'page_obj': page_obj}
    return render(request, 'profilepage/profile-list.html', context)


def friend_list(request):
    """ A view to return a list of all user profile pages """

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))

    user = get_object_or_404(user_model, username=request.user.username)

    friends = Friend.objects.friends(user)

    friendship_requests = Friend.objects.requests(user)

    request_sent = Friend.objects.sent_requests(user)

    context = {'userinfo': userinfo, 'requests': friendship_requests,
               'request_sent': request_sent,
               "friends": friends, get_friendship_context_object_name(): user,
               "friendship_context_object_name": get_friendship_context_object_name()}
    return render(request, 'profilepage/friend-list.html', context)


register = template.Library()


def others_profile(request, username):
    """ A view to return other users profile page """

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=username))
    print(userinfo.user.id)

    currentUserInfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))
    print(currentUserInfo.premium_member)

    check_friendship = Friend.objects.are_friends(
        userinfo.user, currentUserInfo.user) == True

    request_sent = Friend.objects.requests(userinfo.user)
    print(request_sent)

    user = get_object_or_404(user_model, username=request.user.username)
    friendship_requests = Friend.objects.requests(user)
    friends = Friend.objects.friends(user)

    data = Post.objects.filter(user=User.objects.get(username=username)).order_by('date_posted').reverse()
    paginator = Paginator(data, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'userinfo': userinfo,  'currentUserInfo': currentUserInfo,
        'request_sent': request_sent,
        'check_friendship': check_friendship, 'data': data,
        'requests': friendship_requests, 'friends': friends,
        'page_obj': page_obj, }
    return render(request, "profilepage/others-profile.html", context)


def record_hearts_view(request, to_username):
    if request.method == 'POST':
        user_hearts = UserDetails.objects.get(user=User.objects.get(
            username=to_username))
        given_hearts = UserDetails.objects.get(user=User.objects.get(
            username=request.user.username))
        user_hearts.received_hearts += 1
        given_hearts.daily_given_hearts += 1
        user_hearts.save()
        given_hearts.save()
    context = {'user_hearts': user_hearts}
    return redirect("/friend_list", context)


@login_required
def add_friend(request, to_username,  template_name="profilepage/friend_request.html"):
    """ Create a FriendshipRequest """
    ctx = {"to_username": to_username}

    if request.method == "POST":
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect("friend_list")

    return render(request, template_name, ctx)


@login_required
def remove_friend(request, to_username, template_name="profilepage/remove_friend.html"):
    """ A view to remove a friend """

    ctx = {"to_username": to_username}

    if request.method == "POST":
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user

        Friend.objects.remove_friend(from_user, to_user)
        return redirect("friend_list")

    return render(request, template_name, ctx)


@login_required
def request_cancel(request, to_user_id, template_name="profilepage/request_cancel.html"):
    """ Cancel a previously created friendship_request_id """
    if request.method == "POST":
        f_request = get_object_or_404(
             request.user.friendship_requests_sent, id = to_user_id
        )
        print(f_request)
        f_request.cancel()
        return redirect("friend_list", {"friendship_request": f_request})

    return render(request, template_name)


@login_required
def received_friend_requests(
    request, friendship_request_id, template_name="profilepage/received_friendship_requests.html"):
    """ A view to decide whether friend request is accepted or not """

    f_request = get_object_or_404(FriendshipRequest,id =friendship_request_id)

    return render(request, template_name, {"friendship_request": f_request})


@login_required
def friendship_accept(request, to_username, template_name="profilepage/received_friendship_requests.html"):
    """ Accept a friendship request """
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=to_username
        )
        f_request.accept()
        return redirect("/friend_list")


@login_required
def friendship_reject(request, friendship_request_id, template_name="profilepage/received_friendship_requests.html"):
    """ Reject a friendship request """
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=to_username
        )
        f_request.reject()
        f_request.remove()
        return redirect("friendship_request_list")
    
    return redirect(
        "friendship_requests_detail", friendship_request_id=friendship_request_id
    )

