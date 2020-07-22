from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from notes.models import Notes


def dashView(request):
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)
		try:
			notes = Notes.objects.filter(user=request.user)
		except Notes.DoesNotExist:
			notes = None
		context ={
			'title': user.username.upper(),
			'user': user,
			'notes': notes,
		}
		return render(request, 'dashboard/dash.html', context)
	return redirect("/login/")


def addNotes(request):
	pass
