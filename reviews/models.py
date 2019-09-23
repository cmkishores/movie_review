from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

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
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def __str__(self):
		return self.movie_name

	def username_req(request):
		usernameauth = None
		if request.user.is_authenticated():
			usernameauth = request.user.username
			return usernameauth


	def get_absolute_url(self):
		return reverse('review',args=[str(self.id)])
# Create your models here.
