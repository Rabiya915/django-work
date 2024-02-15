from django.contrib import admin
from django.urls import path, include
from myapp import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login.html/', views.user_login, name='login'),
    path('login.html/forms.html/', views.forms, name='Add new Posts'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]