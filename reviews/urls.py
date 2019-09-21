from django.urls import path
from .views import ReviewsListView,ReviewsDetailView,AddReviewView,DeleteReviewView,EditReviewView
urlpatterns= [
	path('reviews/',ReviewsListView.as_view(),name='home'),
	path('reviews/<int:pk>/',ReviewsDetailView.as_view(),name='review'),
	path('reviews/new/', AddReviewView.as_view(),name='addreview'),
	path('reviews/<int:pk>/edit',EditReviewView.as_view(),name='editreview'),
	path('reviews/<int:pk>/delete/',DeleteReviewView.as_view(),name='deletereview'),
]