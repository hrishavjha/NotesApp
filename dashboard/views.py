from django.shortcuts import render, redirect
# from accounts.models import ExtendedUser
from django.contrib.auth.models import User


def dashView(request):
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)
		context = {
			'title': user.username,
			'user': user,
		}
		return render(request, 'dashboard/dash.html', context)
	return redirect("/login/")
