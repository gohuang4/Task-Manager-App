from django.views.generic.list import ListView
from tasks.models import Task
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/new.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.tasks = self.request.user
        item.save()
        return redirect("show_project", pk=item.id)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/edit.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
