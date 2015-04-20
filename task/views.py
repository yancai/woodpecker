#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'views.py'

"""Documentation"""
from datetime import datetime
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, UpdateView
from common.static import TASK_STATUS
from common.utils import MyPaginator, LoginRequiredMixin
from task.forms import TaskAddForm, TaskDetailForm
from task.models import Task


class TaskListView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        tasks_list = user.task_set.all().order_by("-id")
        paginator = MyPaginator(tasks_list, per_page=5, max_range=3)

        page = request.GET.get("page")

        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

        form = TaskAddForm(
            initial={
                "task_status": TASK_STATUS.TODO,
                "start_date": datetime.now().date(),
            }
        )
        return render(request, "task/task_list.html", {
            "tasks": tasks,
            "form": form
        })


class TaskDetailView(UpdateView):
    model = Task
    form_class = TaskDetailForm
    template_name = "task/task_detail.html"
    success_url = "/task/"


class TaskAddView(View):
    def post(self, request, *args, **kwargs):
        form = TaskAddForm(request.POST)
        user = request.user

        if form.is_valid():
            task = Task(
                name=form.cleaned_data["name"],
                task_status=form.cleaned_data["task_status"],
                start_date=form.cleaned_data["start_date"],
                start_time=form.cleaned_data["start_time"],
                # users=(user,)
            )
            try:
                task.save()
                task.users.add(user)
            except Exception as e:
                return HttpResponse(render(request, "task/task_list.html", {"form": form}))

            return HttpResponseRedirect(reverse("task_list"))
        else:
            tasks_list = user.task_set.all().order_by("-id")
            paginator = MyPaginator(tasks_list, per_page=5, max_range=3)
            tasks = paginator.page(1)
            return render(request, "task/task_list.html", {
                "form": form,
                "tasks": tasks,
            })

if __name__ == "__main__":
    pass