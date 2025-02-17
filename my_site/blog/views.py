from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    pass
    # return render(request, 'posts.html')


def post_detail(request, slug):
    pass
    # return render(request, 'post_detail.html')
