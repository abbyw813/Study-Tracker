from django.shortcuts import render, redirect
from studytrackerapp.models import Assignment, Project, Test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotAllowed
from django.urls import reverse
from studytrackerapp.models import UserProfile
from studytrackerapp.forms import UserRegistrationForm
from studytrackerapp.forms import BioUpdateForm

def homepage(request):
    return render(request, 'home/homepage.html')
def search_results(request):
    query = request.GET.get('query')
    return render(request, 'home/search_results.html', {'query': query})

def assignment_list(request):
    assignments = Assignment.objects.all()
    print(assignments)  
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'tests/test_list.html', {'tests': tests})

def create_assignment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        assignment = Assignment(title=title, due_date=due_date)
        assignment.save()
        return redirect('assignment_list')
    return render(request, 'assignments/create_assignment.html')

def create_project(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        project = Project(subject=subject, date=date)
        project.save()
        return redirect('project_list')
    return render(request, 'projects/create_project.html')

def create_test(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        test = Test.objects.create(subject=subject, date=date)
        return redirect('test_list')
    return render(request, 'tests/create_test.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  

@login_required
def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = BioUpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BioUpdateForm(instance=user_profile)

    return render(request, 'profile.html', {'user_profile': user_profile, 'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  
            return redirect('profile')  

    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})

def study_tips_view(request):
    return render(request, 'study_tips.html')


def delete_test(request, test_id):
    if request.method == 'POST':
        try:
            test = Test.objects.get(id=test_id)
            test.delete()
            return redirect('test_list')
        except Test.DoesNotExist:
            return render(request, 'error.html', {'error': 'Test does not exist'})
    return render(request, 'error.html', {'error': 'Method not allowed'})

def delete_project(request, project_id):
    if request.method == 'POST':
        try:
            project = Project.objects.get(id=project_id)
            project.delete()
            return redirect('project_list')
        except Project.DoesNotExist:
            return render(request, 'error.html', {'error': 'Project does not exist'})
    return HttpResponseNotAllowed(['POST'])

def delete_assignment(request, assignment_id):
    if request.method == 'POST':
        try:
            assignment = Assignment.objects.get(id=assignment_id)
            assignment.delete()
            return redirect('assignment_list')
        except Assignment.DoesNotExist:
            return render(request, 'error.html', {'error': 'Assignment does not exist'})
    return render(request, 'error.html', {'error': 'Method not allowed'})
