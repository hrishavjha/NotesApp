from django.shortcuts import render, redirect


def homeView(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	return render(request, "home/home.html", {
		"title": "NotesApp | Home",
	})