from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import djstripe
from django.contrib.auth import authenticate, login
from .models import UserDetails
import stripe
import json
from django.http import JsonResponse
from djstripe.models import Product
from .forms import SignupForm, UserProfileForm
from django.http import HttpResponse
from pprint import pprint
from profilepage.views import userprofile

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

# https://www.ordinarycoders.com/blog/article/django-stripe-monthly-subscription used to get subscription with stripe

@login_required
def checkout(request):

    if request.method == 'GET':
        #print("USER")
        #print(request.user)
        #print("USER.userprofile")
        #print(request.user.userprofile)
        #print("USER.userprofile.subscription")
        #print(request.user.userprofile.subscription)
        if request.user.userprofile.subscription is None:
            products = Product.objects.all()

            context = {"products": products}
            return render(request, "payment_method/checkout.html", context)        
        elif request.user.userprofile.subscription.cancel_at_period_end == True:
            return redirect(cancelledSubscription)
        
        else:

            return redirect(complete)


@login_required
def create_sub(request):

    if request.method == 'POST':
        print("CREATE_SUB POST")
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

        try:
            # This creates a new Customer and attaches
            # the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )

            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(
                customer)
            request.user.customer = djstripe_customer

            # At this point, associate the ID of the Customer object with your
            # own internal representation of a customer, if you have one.

            # Subscribe the user to the subscription created
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )

            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(
                subscription
            )

            #print("########## djstripe_subscription")
            #pprint(vars(djstripe_subscription))

            request.user.userprofile.subscription = djstripe_subscription
            request.user.userprofile.save()

            return JsonResponse(subscription)
        except Exception as e:
            print("EXCEPTION")
            print(e.args[0])
            return JsonResponse({'error': (e.args[0])}, status=403)
        else:
            print("REQUEST METHOD NOT ALLOWED")
            return HTTPresponse('request method not allowed')


def complete(request):
    return render(request, "payment_method/complete.html")

def cancelledSubscription(request):
    return render(request, "payment_method/resubscribe.html")


def cancel(request):
    if request.user.is_authenticated:

        stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY
        sub_num = request.user.userprofile.subscription
        print(sub_num.cancel_at_period_end)

        try:
            sub_num.update(cancel_at_period_end = True)
            sub_num.save

        except Exception as e:
            print("ERROR")
            print(e.args[0])
            return JsonResponse({'error': (e.args[0])}, status =403)

       #     if request.user.is_authenticated:
        #stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

       # stripe_subscription = stripe.Subscription.retrieve(request.user.userprofile.subscription.id)
        #stripe_subscription.id.cancel_at_period_end = True
       # stripe_subscription.save()

    return redirect("userprofile")


def resubscribe(request):
    if request.user.is_authenticated:

        stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY
        sub_num = request.user.userprofile.subscription
        print(sub_num.cancel_at_period_end)

        try:
            sub_num.update(cancel_at_period_end = False)
            sub_num.save



        except Exception as e:
            print("ERROR")
            print(e.args[0])
            return JsonResponse({'error': (e.args[0])}, status =403)

    return redirect("userprofile")
