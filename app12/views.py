from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
import requests

# Home page → list all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, "project_list.html", {"projects": projects})

# Create new project
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "project_form.html", {"form": form})

# Update project
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "project_form.html", {"form": form})

# Delete project
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    return render(request, "project_delete.html", {"project": project})

# API integration → GitHub repos
def github_repos(request, username):
    url = f"https://api.github.com/users/{username}/repos"
    repos = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
    except Exception as e:
        print("Error:", e)
    return render(request, "github.html", {"repos": repos, "username": username})

# Dashboard → simple chart
def dashboard(request):
    count = Project.objects.count()
    return render(request, "dashboard.html", {"count": count})
