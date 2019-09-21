from django.db import models
from django.urls import reverse

class Reviews(models.Model):
	movie_name = models.CharField(max_length=50)
	release_year = models.CharField(max_length=4)
	review = models.TextField()
	author = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

	def __str__(self):
		return self.movie_name

	def username_req(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

# Create your models here.
