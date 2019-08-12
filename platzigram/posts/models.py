from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
# 	"""User model"""
# 	# Django agrega id por defecto

# 	email    = models.EmailField(unique=True)
# 	password = models.CharField(max_length=100)
	
# 	first_name = models.CharField(max_length=100)
# 	last_name  = models.CharField(max_length=100)

# 	is_admin = models.BooleanField(default=False)
	
# 	bio = models.TextField(blank=True)
	
# 	birthDate = models.DateField(blank=True, null=True)
# 	created   = models.DateField(auto_now_add=True)
# 	modified  = models.DateTimeField(auto_now=True)

# 	def __str__(self):
# 		return self.email

class Post(models.Model):
	# Post model

	#Cascade, Protected, set null
	user    = models.ForeignKey(User,on_delete=models.CASCADE)
	# profile  = models.ForeignKey(Profile, on_delete=models.CASCADE)
	profile  = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
	title   = models.CharField(max_length=255)
	photo   = models.ImageField(upload_to='posts/photos')
	created = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} by @{}'.format(self.title,self.user.username)