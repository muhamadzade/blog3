from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def post100(request):
    me = User.objects.get(username='admin')
    for i in range(100, 200):
        now = timezone.now()
        title = f"Title {i}"
        text = f"text {i}"
        Post.objects.create(author=me, title=title, text=text).publish()
    return HttpResponse('100 post is created')
    # Post.save()
