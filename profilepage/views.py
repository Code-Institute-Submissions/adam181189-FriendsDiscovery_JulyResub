from django.shortcuts import render, redirect
from .forms import PostForm
from django.views.generic import ListView
from .models import addPost
from django.contrib.auth.models import User




# Create your views here.
def userprofile(request):
    """ A view to return the users profile page """
    data = addPost.objects.all()
    context = {'data': data}
    return render(request, "profilepage/userprofile.html", context)





def newpost(request):
    """ A view to return the users profile page """
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
