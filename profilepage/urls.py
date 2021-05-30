from django.contrib import admin
from django.urls import path
from . import views
try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url
from friendship.views import (
    all_users,
    block_add,
    block_remove,
    blockers,
    blocking,
    follower_add,
    follower_remove,
    followers,
    following,
    friendship_accept,
    friendship_add_friend,
    friendship_cancel,
    friendship_reject,
    friendship_request_list,
    friendship_request_list_rejected,
    friendship_requests_detail,
    view_friends,
)


urlpatterns = [
    path('userprofile', views.userprofile, name='userprofile'),
    path('mypostprofile', views.mypostprofile, name='mypostprofile'),
    path('newpost', views.newpost, name='newpost'),
    path('update_info', views.update_info, name='update_info'),
    path('update_image', views.update_image, name='update_image'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('friend_list', views.friend_list, name='friend_list'),
    path('add_friend/<str:to_username>/', views.add_friend, name='add_friend'),
    path('add_friend/<str:to_username>/', views.add_friend, name='add_friend'),
    path(
        'received_friend_requests/<int:friendship_request_id>', 
        views.received_friend_requests, 
        name='received_friend_requests'),
    path(
        'friendship_accept/<str:to_username>', 
        views.friendship_accept, 
        name='friendship_accept'),
    path(
        'remove_friend/<str:to_username>', 
        views.remove_friend, 
        name='remove_friend'),
    path(
        'request_cancel/<int:to_user_id>/', 
        views.request_cancel, 
        name='request_cancel'),
    path(
        'record_hearts_view/<str:to_username>/', 
        views.record_hearts_view, 
        name='record_hearts_view'),
    path(
        'others-profile/<str:username>/', 
        views.others_profile, 
        name='others_profile'),
    path(
        'membership_info', 
        views.membership_info, 
        name='membership_info'),
    path(
        'post/<int:post_id>/', 
        views.editPost, 
        name='post-update'),
    path(
        'reject_friendship/<int:friendship_request_id>', 
        views.reject_friendship, 
        name='reject_friendship'),
    path(
        'delete_post/<int:post_id>/', 
        views.delete_post, 
        name='delete_post'),
    
    # friendship-django
    url(regex=r"^users/$", view=all_users, name="friendship_view_users"),
    url(
        regex=r"^friends/(?P<username>[\w-]+)/$",
        view=view_friends,
        name="friendship_view_friends",
    ),
    url(
        regex=r"^friend/add/(?P<to_username>[\w-]+)/$",
        view=friendship_add_friend,
        name="friendship_add_friend",
    ),
    url(
        regex=r"^friend/accept/(?P<friendship_request_id>\d+)/$",
        view=friendship_accept,
        name="friendship_accept",
    ),
    url(
        regex=r"^friend/reject/(?P<friendship_request_id>\d+)/$",
        view=friendship_reject,
        name="friendship_reject",
    ),
    url(
        regex=r"^friend/cancel/(?P<friendship_request_id>\d+)/$",
        view=friendship_cancel,
        name="friendship_cancel",
    ),
    url(
        regex=r"^friend/requests/$",
        view=friendship_request_list,
        name="friendship_request_list",
    ),
    url(
        regex=r"^friend/requests/rejected/$",
        view=friendship_request_list_rejected,
        name="friendship_requests_rejected",
    ),
    url(
        regex=r"^friend/request/(?P<friendship_request_id>\d+)/$",
        view=friendship_requests_detail,
        name="friendship_requests_detail",
    ),
    url(
        regex=r"^followers/(?P<username>[\w-]+)/$",
        view=followers,
        name="friendship_followers",
    ),
    url(
        regex=r"^following/(?P<username>[\w-]+)/$",
        view=following,
        name="friendship_following",
    ),
    url(
        regex=r"^follower/add/(?P<followee_username>[\w-]+)/$",
        view=follower_add,
        name="follower_add",
    ),
    url(
        regex=r"^follower/remove/(?P<followee_username>[\w-]+)/$",
        view=follower_remove,
        name="follower_remove",
    ),
    url(
        regex=r"^blockers/(?P<username>[\w-]+)/$",
        view=blockers,
        name="friendship_blockers",
    ),
    url(
        regex=r"^blocking/(?P<username>[\w-]+)/$",
        view=blocking,
        name="friendship_blocking",
    ),
    url(
        regex=r"^block/add/(?P<blocked_username>[\w-]+)/$",
        view=block_add,
        name="block_add",
    ),
    url(
        regex=r"^block/remove/(?P<blocked_username>[\w-]+)/$",
        view=block_remove,
        name="block_remove",
    ),
]
