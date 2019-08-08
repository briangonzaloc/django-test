#POSTS application module
from django.apps import AppConfig

# https://docs.djangoproject.com/en/2.2/ref/applications/

class PostsConfig(AppConfig):
	#post applications setting
    name = 'posts'
    verbose_name = 'Posts'
