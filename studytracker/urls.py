"""
URL configuration for studytracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studytrackerapp import views
from studytrackerapp.views import homepage, search_results, assignment_list, project_list, test_list, create_assignment, create_project, create_test
from studytrackerapp.views import user_login, user_logout
from studytrackerapp.views import profile_view
from studytrackerapp.views import user_registration
from django.shortcuts import redirect
from studytrackerapp.views import study_tips_view
from studytrackerapp.views import delete_test
from studytrackerapp.views import delete_project
from studytrackerapp.views import delete_assignment

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('search/', search_results, name='search_results'),
    path('assignments/', assignment_list, name='assignment_list'),
    path('assignments/delete/<int:assignment_id>/', delete_assignment, name='delete_assignment'),
    path('projects/', project_list, name='project_list'),
    path('tests/', test_list, name='test_list'),
    path('assignments/create/', create_assignment, name='create_assignment'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/delete/<int:project_id>/', delete_project, name='delete_project'),
    path('tests/create/', create_test, name='create_test'),
    path('tests/delete/<int:test_id>/', delete_test, name='delete_test'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('register/', user_registration, name='register'),
    path('study-tips/', study_tips_view, name='study_tips'),
]
