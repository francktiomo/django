from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']

        if entered_username == '':
            return render(request, 'reviews/review.html', {
                'error': 'Please enter a username'
            })
        print(entered_username)
        return HttpResponseRedirect('thx/')
    return render(request, 'reviews/review.html', {
        'error': ''
    })


def thx(request):
    return render(request, 'reviews/thx.html')
