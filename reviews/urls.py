from django.urls import path
from .views import ReviewsListView,ReviewsDetailView,AddReviewView,DeleteReviewView,EditReviewView,SearchReviewView
urlpatterns= [
	path('',ReviewsListView.as_view(),name='home'),
	path('<int:pk>/',ReviewsDetailView.as_view(),name='review'),
	path('new/', AddReviewView.as_view(),name='addreview'),
	path('<int:pk>/edit',EditReviewView.as_view(),name='editreview'),
	path('<int:pk>/delete/',DeleteReviewView.as_view(),name='deletereview'),
	path('search/', SearchReviewView.as_view(),name='search'),
]