# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#Utilities
from datetime import datetime

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# posts = [
# 	{
# 		'title' : 'Mont Balc',
# 		'user'  : {
# 			'name'    : 'Yesica cortes',
# 			'picture' : 'https://picsum.photos/60/60/?image=1027'
# 		},
# 		'timestamp' : datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
# 		'photo'     : 'https://picsum.photos/800/600/?image=1036'
# 	},
# 	{
# 		'title'      : 'via lactea',
# 		'user'      : {
# 			'name' : 'C. Vander',
# 			'picture': 'https://picsum.photos/60/60/?image=1005'
# 		},
# 		'timestamp' : datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
# 		'photo'     : 'https://picsum.photos/800/800/?image=903'
# 	},
# 	{
# 		'title'      : 'Nuevo auditorio',
# 		'user'      : {
# 			'name' : 'Thespinsd',
# 			'picture': 'https://picsum.photos/60/60/?image=883'
# 		},
# 		'timestamp' : datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
# 		'photo'     : 'https://picsum.photos/500/700/?image=1076'
# 	}
# ]

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

@login_required
def list_posts(request):
	#dentro de cada aplicacion en el folder template lo busca por que esta definido en setting.py
	#reuqes para agregar contesto, nombre del template, context:dictionary
	posts = Post.objects.all().order_by('-created')
	return render(request, 'posts/feed.html', {'posts' : posts})

@login_required
def create_post(request):
	print('create post')
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('feed')
	else:
		form = PostForm()

	return render(
		request=request,
		template_name='posts/new.html',
		context={
			'form'    : form,
			'user'    : request.user,
			'profile' : request.user.profile
		})

