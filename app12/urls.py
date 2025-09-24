from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("create/", views.project_create, name="project_create"),
    path("update/<int:pk>/", views.project_update, name="project_update"),
    path("delete/<int:pk>/", views.project_delete, name="project_delete"),
    path("github/<str:username>/", views.github_repos, name="github_repos"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
