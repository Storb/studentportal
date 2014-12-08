from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Group, Student
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from students.forms import StudentForm



class GroupList(ListView):
    model = Group
    template_name = 'group/groups_list.html'


class GroupUpdate(UpdateView):
    model = Group
    template_name = 'group/update.html'

    def get_success_url(self):
        return reverse('group_detail', args=(self.object.pk, ))


class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('groups_list')
    template_name = 'group/confirm_delete.html'


class GroupCreate(CreateView):
    model = Group
    template_name = 'group/create.html'

    def get_success_url(self):
        return reverse('group_detail', args=(self.object.pk, ))


class GroupDetail(DetailView):
    model = Group
    template_name = 'group/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_form'] = StudentForm(initial={'group': self.object})
        return context

    def post(self, request, pk):
        import ipdb;ipdb.set_trace()
        self.object = Group.objects.get(id=pk)
        context = self.get_context_data()
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return self.render_to_response(context)
        context['student_form'] = form
        return self.render_to_response(context)


class StudentDetail(DetailView):
    model = Student
    template_name = 'student/detail.html'



class StudentList(ListView):
    model = Student
    template_name = 'student/students_list.html'


class StudentCreate(CreateView):
    model = Student
    template_name = 'student/create.html'

    def get_success_url(self):
        return reverse('student_detail', args=(self.object.pk, ))


class StudentDelete(DeleteView):
    model = Student
    template_name = 'student/delete.html'

    def get_success_url(self):
        return reverse('group_detail', args=(self.object.pk, ))


class StudentUpdate(UpdateView):
    model = Student
    template_name = 'student/update.html'

    def get_success_url(self):
        return reverse('student_detail', args=(self.object.pk, ))

class SettingShow(TemplateView):
    template_name = "group/settings_show.html"


class BaseView(TemplateView):
    template_name = "base.html"
