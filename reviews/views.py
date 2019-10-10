from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from django.db.models.query_utils import Q
import stripe

from django.contrib.auth.models import Permission
from django.urls import reverse_lazy

from .models import Reviews
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY



class ReviewsListView(ListView):
	model = Reviews
	template_name = 'home.html'
	context_object_name = 'reviewlist'
	login_url='login'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['stripe_key'] = settings.STRIPE_TEST_PUBLIC_KEY
		return context


def charge(request):


	# takes the permission we set in the model and access using codename
	permission = Permission.objects.get(codename='special_access')
	
	#get the current user credentials

	u= request.user

	#change the permission of user after payment

	u.user_permissions.add(permission)

	if request.method == 'POST':
		charge = stripe.Charge.create(
			amount = 1000,
			currency='usd',
			description='Purchase all stories',
			source=request.POST['stripeToken']
			)
		return render(request, 'done.html')



class ReviewsDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
	model = Reviews
	template_name = 'review.html'
	permission_required = 'reviews.special_access'
	def get_permission_denied_message(self):
		
		permission_denied_message = "You dont have permission to view the review. Please buy a membership to read reviews."
		return self.permission_denied_message

	def get_redirect_field_name(self):
		redirect_field_name = ''
		return self.redirect_field_name

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
	

class SearchReviewView(ListView):
	model = Reviews
	template_name = 'searchview.html'
	context_object_name = 'searchreviewlist'

	# queryset = Reviews.objects.filter(movie_name='Lucifer')
	def get_queryset(self):
		query = self.request.GET['q']
		return Reviews.objects.filter(movie_name__contains=query)

