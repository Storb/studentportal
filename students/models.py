from django.db import models
from django.db.models.signals import pre_delete, post_save
import datetime


class Group(models.Model):
    name = models.CharField(max_length=50)
    elder = models.OneToOneField('Student', related_name='group_elder',
                                 blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group, related_name='students', blank=True, null=True)
    surname = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    card_number = models.IntegerField(max_length=10)
    date_birthday = models.DateField('date birthday')

    def __str__(self):
        return '%s %s %s' % (self.surname, self.first_name, self.last_name, )


class Report(models.Model):
    name_model = models.CharField(max_length=20)
    what_made = models.CharField(max_length=20)
    date_change = models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.name_model, self.what_made, self.date_change)


def delete(sender, instance=None, **kwargs):
    object_d = instance
    if object_d._meta.model_name != 'report':
        name_model = object_d._meta.model_name
        what_made = "Delete"
        date_change = datetime.datetime.now()
        report_temp = Report(name_model=name_model, what_made=what_made,
                             date_change=date_change)
        report_temp.save()


def change_or_add(sender, created, **kwargs):
    object_ch = kwargs.get("instance")
    if object_ch._meta.model_name != "report":
        object_c = kwargs.get("instance")
        name_model = object_c._meta.model_name
        date_change = datetime.datetime.now()
        if not created:
            what_made = "Change"
        else:
            what_made = "Add"
        report_temp = Report(name_model=name_model, what_made=what_made,
                             date_change=date_change)
        report_temp.save()


pre_delete.connect(delete, sender=Group)
post_save.connect(change_or_add, sender=Group)

pre_delete.connect(delete, sender=Student)
post_save.connect(change_or_add, sender=Student)