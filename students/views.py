from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Group, Student
from django.http import HttpResponseRedirect
from .forms import GroupForm, StudentForm
from django.core.urlresolvers import reverse
from django.template import RequestContext



def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group_list'))
        context = {'form': form}
        return render(request, 'group/group_create.html', context)
    else:
        form = GroupForm()
        context = {'form': form}
        return render(request, 'group/group_create.html', context)

def group_delete(request, pk):
    Group.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('group_list'))

def group_confirm_delete(request):
    return render(request, 'group/group_confirm_delete.html')


def group_update(request, pk):
    instance = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group_list'))
        context = {'form': form}
        return render(request, 'group/group_update.html', context)
    else:
        form = GroupForm(instance=instance)
        context = {'form': form}
        return render(request, 'group/group_update.html', context)


def group_list(request):

    list = Group.objects.all()
    context = {'list': list}

    return render(request, 'group/group_list.html', context)


def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    student_list = group.students.all()
    if group.students.filter(group_elder__isnull=False):
        elder = group.students.filter(group_elder__isnull=False)[0]
    else:
        elder = 'None'
    context = {'student_list':student_list, 'group':group.name,
               'elder': elder, 'group_pk':group.pk
               }
    return render(request, 'group/detail.html', context)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student_list'))
        context = {'form':form}
        return render(request, 'student/student_create.html',context)
    else:
        form = StudentForm
        context = {'form':form}
        return render(request,'student/student_create.html', context)


def student_list(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'student/student_list.html', context)


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'first_name':student.first_name, 'last_name':student.last_name,
               'surname':student.surname, 'card_number': student.card_number,
               'date_birthday':student.date_birthday,'pk': pk
               }
    return render(request, 'student/detail.html',context)


def student_update(request, pk):
    instance = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("student_list"))
        context = {'form': form}
        return render(request, 'student/student_update.html', context)
    else:
        form = StudentForm(instance=instance)
        context = {'form': form}
        return render(request, 'student/student_update.html', context)


def student_confirm_delete(request,pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'student/student_confirm_delete.html', context)


def student_delete(request, pk):
    Student.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('student_list'))



def base(request):
    return render(request, 'base.html')



def settings_show(request):
    return render(request, 'group/settings_show.html')

def custom_tags(request):
    student = get_object_or_404(Student,  id = 1)
    context = {'student':  student}
    return render(request, 'custom_tags.html', context )

# def elder_list(request):
#     elder_list = Student.objects.filter(elder__isnull=False)
#     context = {'elder_list':elder_list}
#     return render(request, 'elder/index.html', context)


# class GroupList(ListView):
#     model = Group
#     template_name = 'group/group.html'


# class GroupUpdate(UpdateView):
#     model = Group
#     success_url = reverse_lazy('group_list')
#     template_name = 'group/group_update.html'


# class GroupDelete(DeleteView):
#     model = Group
#     success_url = reverse_lazy('group_list')
#     template_name = 'group/group_confirm_delete.html'