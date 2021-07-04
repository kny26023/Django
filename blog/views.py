from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts= Post.objects.all().order_by('-pk')   #역순은 -

    return render(
        request, 
        'blog/index.html',
        {
            'posts':posts
        }
    )