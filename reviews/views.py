from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from django.urls import reverse_lazy

from .models import Reviews

class ReviewsListView(ListView):
	model = Reviews
	template_name = 'home.html'
	context_object_name = 'reviewlist'

class ReviewsDetailView(DetailView):
	model = Reviews
	template_name = 'review.html'

class AddReviewView(CreateView):
	model = Reviews
	template_name = 'addreview.html'
	fields = ['movie_name','release_year','review','author','rating']

class EditReviewView(UpdateView):
	model = Reviews
	template_name = 'updatereview.html'
	fields = ['movie_name', 'release_year', 'review','rating']

class DeleteReviewView(DeleteView):
	model = Reviews
	template_name = 'deletereview.html'
	success_url = reverse_lazy('home')
