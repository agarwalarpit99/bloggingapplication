from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
class newuserentry(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=15)
	password=models.CharField(max_length=50)
	class Meta:
		db_table="newuserentry"	
class blogpost(models.Model):
	author=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	class Meta:
		db_table="blogpost"
	def __str__(self):
		return self.title

	