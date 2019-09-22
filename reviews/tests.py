from django.test import TestCase

from .models import Reviews
from django.urls import reverse, reverse_lazy


class ReviewsTest(TestCase):
	def setUp(self):
		'''This function is for creating
		dummy data for the testing'''
		self.post = Reviews.objects.create(movie_name='Test',release_year='2019', review='abcd', author='test', rating='5')



	def test_review_content(self):
		review_object = Reviews.objects.get(pk=1)
		expected_object_name = f'{review_object.movie_name}'
		expected_object_release = f'{review_object.release_year}'
		expected_object_review = f'{review_object.review}'
		expected_object_author = f'{review_object.author}'
		self.assertEqual(expected_object_name,'Test')
		self.assertEqual(expected_object_release, '2019')
		self.assertEqual(expected_object_review, 'abcd')
		return self.assertEqual(expected_object_author, 'test')

	def test_movielist_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test')
		self.assertTemplateUsed(response, 'home.html')

	def test_movie_details(self):
		response = self.client.get('/reviews/1/')
		no_response = self.client.get('/reviews/100/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'abcd')
		self.assertTemplateUsed(response, 'review.html')
		
	def test_newreview_view(self):
		response = self.client.post(reverse('addreview'),{
			'movie_name' : 'test2',
			'release_year' : '2019',
			'review' : 'good',
			'author' : 'testing',
			'rating' : '4',
 			})
		#self.assertEqual(response.status_code, 302)
		#self.assertContains(response,'good')
		

	def test_reviewedit_view(self):
		response = self.client.post(reverse('editreview', args='1'),{
			'movie_name' : 'testedit',
			})
		#self.assertContains(response, 'testedit')
		self.assertEqual(response.status_code, 200)
		
	def test_delete_view(self):
		response = self.client.get(reverse_lazy('deletereview',args='1'))

	
		self.assertEqual(response.status_code,200)

# Create your tests here.
