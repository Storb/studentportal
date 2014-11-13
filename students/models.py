from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=50)
    elder = models.ForeignKey("Student", related_name='group_elder',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail',kwargs={'pk':self.pk})


class Student(models.Model):
    group = models.ForeignKey(Group, related_name='student')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    card_number = models.IntegerField(max_length=10)
    date_birthday = models.DateField('date birthday')


    def __str__(self):
        return '%s %s %s' %(self.surname, self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student_detail',kwargs={'pk':self.pk})


# class Contact(User):
#     def __str__(self):
#         return ' '.join([self.first_name, self.last_name])
#
#     def get_absolute_url(self):
#         return reverse('contacts-view', kwargs={'pk': self.id})