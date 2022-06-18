from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from projects.models import Project
from django.views.generic.edit import CreateView
from django.shortcuts import redirect


# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "project_list"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project_detail"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/new.html"
    fields = ["name", "description", "members"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.projects = self.request.user
        item.save()
        return redirect("show_project")
