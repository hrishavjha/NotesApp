from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from home.views import *
from accounts.views import *
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', homeView, name="home"),
    path('login/', loginView, name="login"),
    path('register/', register_view, name="register"),
    path('dashboard/', dashView, name="dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
