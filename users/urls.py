from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#from djstripe import webhooks
#from .webhooks import webhook


urlpatterns = [
    path('', views.index, name='index'),
    path('extendedSignup', views.extendedSignup, name='extendedSignup'),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path('checkout', views.checkout, name='checkout'),
    path('create_sub', views.create_sub, name='create_sub'),
    path('complete', views.complete, name='complete'),
    path('cancel', views.cancel, name='cancel'),
    path('cancelledSubscription', views.cancelledSubscription, name='cancelledSubscription'),
    path('resubscribe', views.resubscribe, name='resubscribe'),
    #path('wh/', webhook, name='webhook'),
]