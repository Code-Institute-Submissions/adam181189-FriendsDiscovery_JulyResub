from django.shortcuts import render
from .forms import PostForm


# Create your views here.
def userprofile(request):
    """ A view to return the users profile page """
    if request.method == 'POST':
        BlogPostForm = PostForm(request.POST)

        if BlogPostForm.is_valid():
            BlogPostForm.instance.user = request.user
            BlogPostForm.save(commit=True)

    else:
        BlogPostForm = PostForm()

    context = {'BlogPostForm': BlogPostForm}
    return render(request, 'profilepage/userprofile.html', context)

