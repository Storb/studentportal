from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, Student
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView


class GroupList(ListView):
    model = Group
    template_name = 'group/groups_list.html'


class GroupUpdate(UpdateView):
    model = Group
    success_url = reverse_lazy('group_list')
    template_name = 'group/update.html'

    def form_valid(self, form):
        super(GroupUpdate, self).form_valid(form)
        return redirect(reverse_lazy("group_detail", args=(self.object.id,)))


class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('groups_list')
    template_name = 'group/confirm_delete.html'


class GroupCreate(CreateView):
    model = Group
    template_name = 'group/create.html'

    def form_valid(self, form):
        super(GroupCreate, self).form_valid(form)
        return redirect(reverse_lazy("group_detail", args=(self.object.id, )))


class GroupDetail(DetailView):
    model = Group
    template_name = 'group/detail.html'


class StudentList(ListView):
    model = Student
    template_name = 'student/students_list.html'


class StudentCreate(CreateView):
    model = Student
    template_name = 'student/create.html'

    def form_valid(self, form):
        super(StudentCreate, self).form_valid(form)
        return redirect(reverse_lazy('student_detail', args=(self.object.id, )))


class StudentDetail(DetailView):
    model = Student
    template_name = 'student/detail.html'


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students_list')
    template_name = 'student/delete.html'


class StudentUpdate(UpdateView):
    model = Student
    success_url = reverse_lazy('students_list')
    template_name = 'student/update.html'

    def form_valid(self, form):
        super(StudentUpdate, self).form_valid(form)
        return redirect(reverse_lazy('student_detail', args=(self.object.id, )))

def settings_show(request):
    return render(request, 'group/settings_show.html')

def custom_tags(request):
    student = get_object_or_404(Student,  id = 1)
    context = {'student':  student}
    return render(request, 'custom_tags.html', context )


def base(request):
    return render(request, 'base.html')