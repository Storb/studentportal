from django.forms import ModelForm
from .models import Group, Student
from django import forms



class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'elder' )


class StudentForm(ModelForm):

    class Meta:
        model = Student


# class GroupForm(ModelForm):
#      class Meta:
#          model = Group