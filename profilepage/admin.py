from django.contrib import admin
from profilepage.models import Post, Heart
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Post)
admin.site.register(Heart)
