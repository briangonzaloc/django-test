# Django
from django.urls import path
# from django.views.generic import TemplateView

# Views
from users import views

app_name    = 'users'
urlpatterns = [

	path(
		route='profile/<str:username>/',
		# view=TemplateView.as_view(template_name='users/detail.html'),
		view=views.UserDetailView.as_view(),
		name='detail',
	),
	# Managment
	path(
		route='login/', 
		view=views.LoginView.as_view(),
		# view=views.login_view, 
		name="login"
	),
	path(
		route='logout/', 
		# view=views.logout_view, 
		view=views.LogoutView.as_view(),
		name="logout"
	),
	path(
		route='signup/', 
		view=views.SignupView.as_view(),
		# view=views.signup, 
		name='signup'
	),
	path(
		route='me/profile/', 
		view=views.UpdateProfileView.as_view(),
		# view=views.update_profile, 
		name='update_profile'
	),
]