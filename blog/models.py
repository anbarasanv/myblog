from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100)
	text = models.TextField()
	published_date = models.DateTimeField(auto_now_add=True)
	thumnail = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.text[:256]+'...'

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, max_length=250, on_delete=models.CASCADE)
	comment = models.CharField(max_length=500, default=None)	
	time = models.DateTimeField(auto_now_add=True)
	# approved = models.BooleanField(default=False)

	# def approved(self):
	# 	self.approved = True
	# 	self.save()
	# def __str__(self):
	# 	return self.body 