from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            entered_username = form.cleaned_data['username']
            return HttpResponseRedirect('thx/')
    else:
      form = ReviewForm()

    return render(request, 'reviews/review.html', {
        'form': form
    })


def thx(request):
    return render(request, 'reviews/thx.html')
