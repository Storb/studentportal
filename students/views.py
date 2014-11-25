from django.shortcuts import render, redirect
from .models import Group, Student
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from students.forms import StudentForm



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

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        context['student_form'] = StudentForm(initial={'group': self.object})
        return context

    def post(self, request, pk):
        self.object = Group.objects.get(id=pk)
        context = self.get_context_data()
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return self.render_to_response(context)
        context['student_form'] = form
        return self.render_to_response(context)


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
    template_name = 'student/delete.html'
    group_id = None
    success_url = reverse_lazy('groups_list', group_id)

    def get_context_data(self, **kwargs):
        import ipdb;ipdb.set_trace()
        context = super(StudentDelete, self).get_context_data(**kwargs)



class StudentUpdate(UpdateView):
    model = Student
    success_url = reverse_lazy('groups_list')
    template_name = 'student/update.html'

    def form_valid(self, form):
        super(StudentUpdate, self).form_valid(form)
        return redirect(reverse_lazy('student_detail', args=(self.object.id, )))


def settings_show(request):
    return render(request, 'group/settings_show.html')


def base(request):
    return render(request, 'base.html')