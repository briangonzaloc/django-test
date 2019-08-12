from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login_view(request):
	#login view
	return render(request,'users/login.html')
