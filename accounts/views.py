from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import ExtendedUser


def register_view(request):
	context = {
		'title': 'Notesapp | Register',
	}
	if request.user.is_authenticated:
		return redirect('dashboard')
	if request.method == "POST":
		password = request.POST.get('password')
		img = request.FILES['profile_img']
		confirmPassword = request.POST.get('cnfrm_password')
		if password == confirmPassword:
			user = User.objects.filter(username=request.POST.get('username'))
			if user.count() > 0:
				return render(request, 'accounts/register.html', {'error': 'Username is already taken.'})
			else:
				user = User.objects.create_user(username=request.POST.get('username'), password=password,
												email=request.POST.get('email'),
												first_name=request.POST.get('firstname'),
												last_name=request.POST.get('lastname'))
				user.save()
				user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
				auth.login(request, user)
				profile = ExtendedUser.objects.create(user=request.user, profile_image=img)
				profile.save()
				return redirect('/dashboard/')
		else:
			return render(request, 'accounts/register.html', {'error': 'Passwords dont match'})
	else:
		return render(request, 'accounts/register.html', context)


def loginView(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	context = {
		'title': 'Notesapp | Login',
	}
	if request.method == "POST":
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('/dashboard/')
		else:
			return render(request, "accounts/login.html", {"error": "Invalid Login Credentials."})
	else:
		return render(request, 'accounts/login.html', context)