# Django
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, FormView, UpdateView


#Exception
# from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
	template_name       ='users/detail.html'
	slug_field          = 'username'
	slug_url_kwarg      = 'username' # same name in path url arguments
	queryset            = User.objects.all()
	context_object_user = 'user' # Define el nombre del objeto que traigamos en el template

	def get_context_data(self, **kwargs):
		# add user's post to context
		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user=user).order_by('-created')
		return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
	template_name = 'users/update_profile.html'
	model = Profile
	fields = ['website', 'biography', 'phone_number', 'picture']

	def get_object(self):
		#return user's profie
		return self.request.user.profile

	def get_success_url(self):
		# return to user's profuile
		username = self.object.user.username
		return reverse('users:detail', kwargs={'username' : username })


# @login_required
# def update_profile(request):
# 	#update a user's profile
# 	profile = request.user.profile

# 	if request.method == 'POST':
# 		form = ProfileForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			data = form.cleaned_data
# 			profile.website      = data['website']
# 			profile.biography    = data['biography']
# 			profile.phone_number = data['phone_number']
# 			profile.picture      = data['picture']
# 			profile.save()
# 			url = reverse('users:detail', kwargs={'username' : request.user.username })
# 			return redirect(url)

# 	else:
# 		form = ProfileForm()

# 	return render(
# 		request       = request, 
# 		template_name = 'users/update_profile.html',
# 		context       = {
# 			'profile': profile,
# 			'user'   : request.user,
# 			'form'   : form,
# 		}
# 	)

class LoginView(auth_views.LoginView):
	template_name = 'users/login.html'


# def login_view(request):
# 	#login a user
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user:
# 			login(request, user)
# 			return redirect('posts:feed') #use url name
# 		else:
# 			error = 'Invalid username and password'
# 			return render(request, 'users/login.html', {'error':'Invalid username and password'})

# 	return render(request, 'users/login.html')


class SignupView(FormView):
	template_name = 'users/signup.html'
	form_class    = SignupForm
	success_url   = reverse_lazy('users:login')

	def form_valid(self,form):
		form.save()
		return super().form_valid(form)

# First approach
# def signup(request):
# 	#sign up view
# 	if request.method == 'POST':
# 		username            = request.POST['username']
# 		passwd              = request.POST['passwd']
# 		passwd_confirmation = request.POST['passwd_confirmation']

# 		if passwd != passwd_confirmation:
# 			return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

# 		try:
# 			user = User.objects.create_user(username=username,password=passwd)
# 		except IntegrityError:
# 			return render(request, 'users/signup.html', {'error': 'Username is already in user'})

# 		user.first_name = request.POST['first_name']
# 		user.last_name  = request.POST['last_name']
# 		user.email      = request.POST['email']
# 		user.save()

# 		profile = Profile(user=user)
# 		profile.save()

# 		return redirect('login')

# 	return render(request, 'users/signup.html')




# def signup(request):
# 	#sign up view
# 	if request.method == 'POST':
# 		form = SignupForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('users:login')
# 	else:
# 		form = SignupForm()

# 	return render(
# 		request=request,
# 		template_name='users/signup.html',
# 		context={'form' : form})

class LogoutView(auth_views.LogoutView):
	template_name = 'users/logged_out.html'

# @login_required
# def logout_view(request):
# 	# Logount a user
# 	logout(request)
# 	return redirect('users:login')

