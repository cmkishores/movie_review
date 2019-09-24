from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query_utils import Q

from django.urls import reverse_lazy

from .models import Reviews

class ReviewsListView(LoginRequiredMixin, ListView):
	model = Reviews
	template_name = 'home.html'
	context_object_name = 'reviewlist'
	login_url='login'

class ReviewsDetailView(LoginRequiredMixin,DetailView):
	model = Reviews
	template_name = 'review.html'

class AddReviewView(LoginRequiredMixin,CreateView):
	model = Reviews
	template_name = 'addreview.html'
	fields = ['movie_name','release_year','review','author','rating','poster']
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class EditReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Reviews
	template_name = 'updatereview.html'
	fields = ['movie_name', 'release_year', 'review','rating','poster']
	
	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user

class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Reviews
	template_name = 'deletereview.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user


class SearchReviewView(LoginRequiredMixin,ListView):
	model = Reviews
	template_name = 'searchview.html'
	context_object_name = 'searchreviewlist'

	# queryset = Reviews.objects.filter(movie_name='Lucifer')
	def get_queryset(self):
		query = self.request.GET['q']
		return Reviews.objects.filter(movie_name__contains=query)

