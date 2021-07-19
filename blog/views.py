from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
# Create your views here.

class PostList(ListView):   #ListView를 쓸 땐 뒤에 _list를 붙여줘야!
    model= Post
    #template_name= 'blog/index.html'
    ordering= '-pk'

    def get_context_data(self, **kwargs):
        context= super(PostList, self).get_context_data()   
        #super: parent class의 객체를 호출하는 메소드
        #모든 내용을 가져오는 메소드! 내가 사용하는 공간 내에서 부모 클래스를 만드는 것!
        context['categories']= Category.objects.all()
        context['no_category_post_count']= Post.objects.filter(category=None).count()
        return context

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