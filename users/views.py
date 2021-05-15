from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import djstripe
from django.contrib.auth import authenticate, login
import stripe
import json
from django.http import JsonResponse
from djstripe.models import Product
from .forms import SignupForm, UserProfileForm
from django.http import HttpResponse

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


@login_required
def checkout(request):
    
    if request.method == 'GET':
        products = Product.objects.all()

        context = {"products": products}
        return render(request, "payment_method/checkout.html", context)
    if request.method == 'POST':
        print("CHECKOUT POST")

@login_required
def create_sub(request):
  if request.method == 'POST':
    print("CREATE_SUB POST")
    # Reads application/json and returns a response
    data = json.loads(request.body)
    payment_method = data['payment_method']
    stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

    print(payment_method)
    print(stripe.api_key)
    
    payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
    djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

    print(payment_method_obj)

    try:
        # This creates a new Customer and attaches the PaymentMethod in one API call.
        customer = stripe.Customer.create(
            payment_method=payment_method,
            email=request.user.email,
            invoice_settings={
                 'default_payment_method': payment_method
            }
        )

        djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
        request.user.customer = djstripe_customer

        # At this point, associate the ID of the Customer object with your
        # own internal representation of a customer, if you have one.
        # print(customer)

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

        djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)
        request.user.subscription = djstripe_subscription
        request.user.save()

        print("SUCCESS")
        print(subscription)

        return JsonResponse(subscription)
    except Exception as e:
        print("EXCEPTION")
        print(e.args[0])
        return JsonResponse({'error': (e.args[0])}, status =403)
    else:
        print("REQUEST METHOD NOT ALLOWED")
        return HTTPresponse('request method not allowed')

def complete(request):
    return render(request, "payment_method/complete.html")
