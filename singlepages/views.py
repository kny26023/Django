from django.shortcuts import render

# Create your views here.
# front

def landing(request):
    return render(
        request,
        'singlepages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'singlepages/about_me.html'
    )