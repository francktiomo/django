from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

from django.http import HttpRequest
from django.views import View

# Create your views here.


class ReviewView(View):
    def get(self, request: HttpRequest):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request: HttpRequest):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thx/')

        return render(request, 'reviews/review.html', {
            'form': form
        })


# def review(request: HttpRequest):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     username=form.cleaned_data['username'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']
#             # )
#             # review.save()
#             form.save()
#             return HttpResponseRedirect('thx/')
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/review.html', {
#         'form': form
#     })

def thx(request):
    return render(request, 'reviews/thx.html')
