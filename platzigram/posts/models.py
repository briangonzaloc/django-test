from django.db import models

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