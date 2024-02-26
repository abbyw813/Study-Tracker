from django.shortcuts import render, redirect
from studytrackerapp.models import Assignment, Project, Test

# Create your views here.
def homepage(request):
    return render(request, 'home/homepage.html')
def search_results(request):
    query = request.GET.get('query')
    # Add your search logic here
    return render(request, 'home/search_results.html', {'query': query})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment_list.html', {'assignments': assignments})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests': tests})

def create_assignment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        assignment = Assignment(title=title, due_date=due_date)
        assignment.save()
        return redirect('assignment_list')
    return render(request, 'create_assignment.html')

def create_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        project = Project(name=name, description=description)
        project.save()
        return redirect('project_list')
    return render(request, 'create_project.html')

def create_test(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        test = Test(subject=subject, date=date)
        test.save()
        return redirect('test_list')
    return render(request, 'create_test.html')



