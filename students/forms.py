from django.forms import ModelForm
from .models import Group, Student
from django import forms



class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'elder' )


class StudentForm(ModelForm):
    card_number = forms.IntegerField(max_value=9999999999)
    class Meta:
        model = Student


# class GroupForm(forms.ModelForm):
#      class Meta:
#          model = Group