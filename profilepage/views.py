from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, updateprofileinfo,\
     updateprofileimage, HeartForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db.models import Q
from .models import Post, updateInfo, Heart
from users.models import UserDetails
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import DetailView
from friendship.models import Friend, Follow, \
    Block, FriendshipRequest, bust_cache
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import template
from datetime import datetime, date

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

    userinfo = UserDetails.objects.get(
        user=User.objects.get(username=request.user.username)
    )

    date_of_birth = userinfo.date_of_birth

    def calculateAge(date_of_birth):

        today = date.today()
        age = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (
                date_of_birth.month, date_of_birth.day))
        )

        return age

    myage = calculateAge(date_of_birth)
    print(myage)

    user = get_object_or_404(
        user_model, username=request.user.username)

    friends = Friend.objects.friends(user)

    data = []
    for post in Post.objects.all().order_by("date_posted").reverse():
        if post.user in friends or \
                str(post.user) == str(request.user.username):
            data.append(post)

    paginator = Paginator(data, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "userinfo": userinfo, "data": data, 
        "page_obj": page_obj, "myage": myage}
    return render(
        request, "profilepage/userprofile.html", context)


def mypostprofile(request):
    """ A view to return the users profile page """

    userinfo = UserDetails.objects.get(
        user=User.objects.get(
            username=request.user.username)
    )

    date_of_birth = userinfo.date_of_birth

    def calculateAge(date_of_birth):

        today = date.today()
        age = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (
                date_of_birth.month, date_of_birth.day))
        )

        return age

    myage = calculateAge(date_of_birth)
    print(myage)

    user = get_object_or_404(
        user_model, username=request.user.username)

    friends = Friend.objects.friends(user)

    data = (
        Post.objects.filter(user=User.objects.get(
            username=request.user.username))
        .order_by("date_posted")
        .reverse()
    )

    paginator = Paginator(data, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "userinfo": userinfo, "data": data, 
        "page_obj": page_obj, "myage": myage}
    return render(request, "profilepage/mypostprofile.html", context)


def update_info(request):
    """ A view to be able to change user info on the profile page """

    if request.method == "POST":
        user = UserDetails.objects.get(
            user=User.objects.get(
                username=request.user.username)
        )
        update_information = updateprofileinfo(
            request.POST, instance=user)

        if update_information.is_valid():

            profile = update_information.save(commit=False)

            profile.save()

            messages.error(request, "Profile Information Updated")

            return redirect("userprofile")

    else:
        userinfo = UserDetails.objects.get(
            user=User.objects.get(username=request.user.username)
        )
        update_information = updateprofileinfo(instance=userinfo)

    context = {"update_information": update_information}
    return render(request, "profilepage/update_info.html", context)


def update_image(request):
    """ A view to be able to change users image on the profile page """

    if request.method == "POST":
        user = UserDetails.objects.get(
            user=User.objects.get(username=request.user.username)
        )
        update_image = updateprofileimage(
            request.POST, request.FILES, instance=user)

        if update_image.is_valid():

            profile_picture = update_image.save(commit=False)

            profile_picture.save()

            messages.error(request, "Profile Image Updated")
            return redirect("userprofile")

    else:
        userinfo = UserDetails.objects.get(
            user=User.objects.get(
                username=request.user.username)
        )
        update_image = updateprofileimage(instance=userinfo)

    context = {"updateprofileimage": updateprofileimage}
    return render(request, "profilepage/update_image.html", context)


def newpost(request):
    """ A view to add a new blog post  """

    if request.method == "POST":
        BlogPostForm = PostForm(request.POST)

        if BlogPostForm.is_valid():
            BlogPostForm.instance.user = request.user
            BlogPostForm.save(commit=True)
            messages.error(request, "Added new post")
            return redirect("userprofile")

    else:
        BlogPostForm = PostForm()

    context = {"BlogPostForm": BlogPostForm}
    return render(request, "profilepage/newpost.html", context)


def editPost(request, post_id):
    """ A view to edit a blog post  """

    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        update_post = PostForm(
            request.POST, request.FILES, instance=post)

        if update_post.is_valid():
            update_post.instance.user = request.user
            update_post.save(commit=True)

            messages.error(request, "Post updated")
            return redirect("userprofile")
    else:
        post = Post.objects.get(id=post_id)
        update_post = PostForm(instance=post)

    context = {
        "update_post": update_post,
        "update_image": update_image,
        "post": post,
    }
    return render(request, "profilepage/update_post.html", context)


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    messages.error(request, "Post Deleted")
    post.delete()

    return redirect("userprofile")


def profile_list(request):

    print("profile_list()")

    """ A view to return a list of all user profile pages """

    userinfo = UserDetails.objects.get(
        user=User.objects.get(
            username=request.user.username)
    )

    data = UserDetails.objects.all()
    paginator = Paginator(data, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "userinfo": userinfo, "data": data, "page_obj": page_obj}
    return render(request, "profilepage/profile-list.html", context)


def friend_list(request):
    """ A view to return a list of all user profile pages """

    userinfo = UserDetails.objects.get(
        user=User.objects.get(username=request.user.username)
    )

    user = get_object_or_404(user_model, username=request.user.username)

    friends = Friend.objects.friends(user)

    friendship_requests = Friend.objects.requests(user)

    request_sent = Friend.objects.sent_requests(user)

    context = {
        "userinfo": userinfo,
        "requests": friendship_requests,
        "request_sent": request_sent,
        "friends": friends,
        get_friendship_context_object_name(): user,
        "friendship_context_object_name": 
            get_friendship_context_object_name(),
    }
    return render(request, "profilepage/friend-list.html", context)


register = template.Library()


def others_profile(request, username):

    """ A view to return other users profile page """

    def hearts_sent_today():
        heartsToday = Heart.objects.filter(
            from_user=request.user, date_posted__date=date.today()
        ).count()
        # print(f'Hearts sent today for {request.user}: {heartsToday}.')

        return heartsToday

    def hearts_received(user):
        heartsReceived = Heart.objects.filter(to_user=user).count()
        # print(f'Hearts received for {user}: {heartsReceived}.')

        return heartsReceived

    userinfo = UserDetails.objects.get(
        user=User.objects.get(username=username))
    # print(userinfo.user.id)

    currentUserInfo = UserDetails.objects.get(
        user=User.objects.get(username=request.user.username)
    )
    print(currentUserInfo.premium_member)

    date_of_birth = userinfo.date_of_birth

    def calculateAge(date_of_birth):

        today = date.today()
        age = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (
                date_of_birth.month, date_of_birth.day))
        )

        return age

    myage = calculateAge(date_of_birth)

    check_friendship = (
        Friend.objects.are_friends(
            userinfo.user, currentUserInfo.user) is True
    )

    request_sent = Friend.objects.requests(userinfo.user)

    request_sent_value = False
    for r in request_sent:
        if str(r) == str(currentUserInfo.user.id):
            request_sent_value = True

    user = get_object_or_404(
        user_model, username=request.user.username)
    friendship_requests = Friend.objects.requests(user)
    friends = Friend.objects.friends(user)

    data = (
        Post.objects.filter(user=User.objects.get(
            username=username))
        .order_by("date_posted")
        .reverse()
    )
    paginator = Paginator(data, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "userinfo": userinfo,
        "currentUserInfo": currentUserInfo,
        "request_sent": request_sent_value,
        "check_friendship": check_friendship,
        "data": data,
        "requests": friendship_requests,
        "friends": friends,
        "page_obj": page_obj,
        "hearts_sent_today": hearts_sent_today(),
        "hearts_received": hearts_received(userinfo.user),
        "myage": myage,
    }
    return render(request, "profilepage/others-profile.html", context)


@login_required
def add_friend(
    request, to_username, 
        template_name="profilepage/friend_request.html"):

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
            messages.error(request, "Request Sent")
            return redirect("friend_list")

    return render(request, template_name, ctx)


@login_required
def remove_friend(
        request, to_username, template_name="profilepage/remove_friend.html"):

    """ A view to remove a friend """

    ctx = {"to_username": to_username}

    if request.method == "POST":
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        messages.error(request, "Friendship removed")

        Friend.objects.remove_friend(from_user, to_user)
        return redirect("friend_list")

    return render(request, template_name, ctx)


@login_required
def request_cancel(
    request, to_user_id, template_name="profilepage/request_cancel.html"
):
    """ Cancel a previously created friendship_request_id """

    getuserinfo = UserDetails.objects.get(
        user=User.objects.get(id=to_user_id))

    userinfo = getuserinfo.user.id

    getcurrentUserInfo = UserDetails.objects.get(
        user=User.objects.get(username=request.user.username)
    )

    currentUserInfo = getcurrentUserInfo.user.id

    if request.method == "POST":
        FriendshipRequest.objects.filter(
            from_user=currentUserInfo, to_user=userinfo
        ).delete()
        bust_cache("requests", userinfo)
        bust_cache("sent_requests", userinfo)

        # Bust reverse requests cache - reverse request might be deleted
        bust_cache("requests", currentUserInfo)
        bust_cache("sent_requests", currentUserInfo)

        return redirect("friend_list")

    return render(
        request,
        template_name,
        {
            "userinfo": userinfo,
            "currentUserInfo": currentUserInfo,
            "getuserinfo": getuserinfo,
            "getcurrentUserInfo": getcurrentUserInfo,
        },
    )


@login_required
def received_friend_requests(
    request,
    friendship_request_id,
    template_name="profilepage/received_friendship_requests.html",
):
    """ A view to decide whether friend request is accepted or not """

    f_request = get_object_or_404(FriendshipRequest, id=friendship_request_id)

    return render(request, template_name, {"friendship_request": f_request})


@login_required
def friendship_accept(
    request, to_username, 
    template_name="profilepage/received_friendship_requests.html"
):
    """ Accept a friendship request """
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=to_username
        )
        f_request.accept()
        return redirect("/friend_list")


@login_required
def reject_friendship(
    request, friendship_request_id, 
    template_name="profilepage/reject_friendship.html"
):
    """ Reject a friendship request """

    print(friendship_request_id)

    getuserinfo = UserDetails.objects.get(
        user=User.objects.get(id=friendship_request_id)
    )

    userinfo = getuserinfo.user.id

    getcurrentUserInfo = UserDetails.objects.get(
        user=User.objects.get(username=request.user.username)
    )

    currentUserInfo = getcurrentUserInfo.user.id

    if request.method == "POST":

        FriendshipRequest.objects.filter(
            to_user=currentUserInfo, from_user=userinfo
        ).delete()
        bust_cache("requests", userinfo)
        bust_cache("sent_requests", userinfo)

        # Bust reverse requests cache - reverse request might be deleted
        bust_cache("requests", currentUserInfo)
        bust_cache("sent_requests", currentUserInfo)

        return redirect("friend_list")

    return render(
        request,
        template_name,
        {
            "userinfo": userinfo,
            "currentUserInfo": currentUserInfo,
            "getuserinfo": getuserinfo,
            "getcurrentUserInfo": getcurrentUserInfo,
        },
    )


@login_required
def record_hearts_view(request, to_username):
    if request.method == "POST":
        heart = Heart.objects.create(
            from_user=User.objects.get(username=request.user.username),
            to_user=User.objects.get(username=to_username),
            date_posted=datetime.now(),
        )
        # heart.save(commit=True)

        return redirect("/friend_list")


@login_required
def membership_info(request):

    return render(request, "profilepage/membership_info.html")
