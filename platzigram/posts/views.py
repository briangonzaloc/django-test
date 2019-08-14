# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


#Utilities
from datetime import datetime

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# def list_posts(request):
# 	""" List existing posts """
# 	content = []
# 	for post in posts:
# 		content.append("""
# 			<p><strong>{name}</strong></p>
# 			<p><small>{user} - {timestamp}<i></i></small></p>
# 			<figure><img src="{picture}" /> </figure>
# 		""".format(**post)) # para no poner post.name, post.user
# 	return HttpResponse('<br>'.join(content))

class PostsFeedView(LoginRequiredMixin,ListView):
	# Return all published posts
	template_name = 'posts/feed.html'
	model = Post
	ordering = ('-created',)
	paginate_by = 30
	context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin,DetailView):
	template_name = 'posts/detail.html'
	queryset = Post.objects.all()
	context_object_name = 'post'


# @login_required
# def list_posts(request):
# 	#dentro de cada aplicacion en el folder template lo busca por que esta definido en setting.py
# 	#reuqes para agregar contesto, nombre del template, context:dictionary
# 	posts = Post.objects.all().order_by('-created')
# 	return render(request, 'posts/feed.html', {'posts' : posts})

class CreatePostView(LoginRequiredMixin, CreateView):
	template_name = 'posts/new.html'
	form_class    = PostForm
	success_url   = reverse_lazy('posts:feed')

	def get_context_data(self, **kwarg):
		# Add data to context
		context = super().get_context_data(**kwarg)
		context['user']    = self.request.user
		context['profile'] = self.request.user.profile
		return context


# @login_required
# def create_post(request):
# 	print('create post')
# 	if request.method == 'POST':
# 		form = PostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('posts:feed')
# 	else:
# 		form = PostForm()

# 	return render(
# 		request=request,
# 		template_name='posts/new.html',
# 		context={
# 			'form'    : form,
# 			'user'    : request.user,
# 			'profile' : request.user.profile
# 		})

