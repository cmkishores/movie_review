from django.db import models
from django.urls import reverse

class Reviews(models.Model):
	RATING = [
	('*','1'),
	('**','2'),
	('***','3'),
	('****','4'),
	('*****','5'),
				]

	movie_name = models.CharField(max_length=50)
	release_year = models.CharField(max_length=4)
	review = models.TextField()
	rating = models.CharField(max_length=50,choices=RATING)
	author = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
	last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
	

	def __str__(self):
		return self.movie_name

	def username_req(request):
		username = None
		if request.user.is_authenticated():
			username =request.user.username
			return username

	def get_absolute_url(self):
		return reverse('review',args=[str(self.id)])
# Create your models here.
