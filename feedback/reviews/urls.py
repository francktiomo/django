from django.urls import path

from . import views

urlpatterns = [
    # path('', views.review),
    path('', views.ReviewView.as_view()),
    path('thx/', views.ThxView.as_view()),
    path('reviews/', views.ReviewsListView.as_view())
    # path('reviews/<int:id>', views.ReviewDetail)
]
