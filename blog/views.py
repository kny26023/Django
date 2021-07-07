from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class PostList(ListView):   #ListView를 쓸 땐 뒤에 _list를 붙여줘야!
    model= Post
    #template_name= 'blog/index.html'
    ordering= '-pk'

'''
def index(request):
    posts= Post.objects.all().order_by('-pk')   #역순은 -

    return render(
        request, 
        'blog/index.html',  #template_name
        {
            'posts':posts
        }
    )
'''

class PostDetail(DetailView):
    model= Post
    #template_name= 'blog/single_post_page.html'

'''
def single_post_page(request, pk):
    post= Post.objects.get(pk= pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post
        }
    )
'''