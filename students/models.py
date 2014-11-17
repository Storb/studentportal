from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, pre_delete, post_save
import datetime


class Group(models.Model):
    name = models.CharField(max_length=50)
    elder = models.ForeignKey("Student", related_name='group_elder',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'pk': self.pk})


class Student(models.Model):
    group = models.ForeignKey(Group, related_name='student')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    card_number = models.IntegerField(max_length=10)
    date_birthday = models.DateField('date birthday')


    def __str__(self):
        return '%s %s %s' % (self.surname, self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})


class Report(models.Model):
    name_model = models.CharField(max_length=10)
    what_made = models.CharField(max_length=15)
    text = models.CharField(max_length=200, blank=True, null=True)
    date_change = models.DateField()

    def __str__(self):
        return "%s %s" % (self.name_model, self.what_made)


def handler_delete(sender, **kwargs):
    object_d = kwargs.get('instance')
    if object_d._meta.module_name != 'report':
        name_model = object_d._meta.module_name
        what_made = "Delete"
        date_change = datetime.datetime.now()
        test = "%s %s, %s" % (what_made, name_model, date_change)
        # print test
        report_temp = Report(name_model=name_model, what_made=what_made, date_change=date_change)
        report_temp.save()


def handler_change(sender, created, **kwargs):
    object_ch = kwargs.get('instance')
    if object_ch._meta.module_name != 'report':
        object_c = kwargs.get('instance')
        name_model = object_c._meta.module_name
        date_change = datetime.datetime.now()
        if not created:
            what_made = "Change"
        else:
            what_made = "Add"
        # print "%s %s, %s" % (what_made, name_model, date_change)
        report_temp = Report(name_model=name_model, what_made=what_made, date_change=date_change)
        report_temp.save()


pre_delete.connect(handler_delete)
post_save.connect(handler_change)