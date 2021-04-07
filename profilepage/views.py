from django.shortcuts import render

# Create your views here.

def userprofile(request):
    """ A view to return the users profile page """

    return render(request, 'profilepage/userprofile.html')