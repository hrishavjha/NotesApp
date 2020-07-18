from django.shortcuts import render


def homeView(request):
	# if request.user.is_authenticated:
	# 	return redirect('dashboard')
	return render(request, "home/home.html", {
		"title": "NotesApp | Home",
	})