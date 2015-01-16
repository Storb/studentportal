from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    elder = models.OneToOneField(
        'Student', related_name='group_elder',
        blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('created',)


class Student(models.Model):
    group = models.ForeignKey(Group, related_name='students')
    created = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birthday = models.DateField('date birthday')
    card_number = models.IntegerField(max_length=10)
    owner = models.ForeignKey(
        'auth.User', related_name='students',
        blank=True, null=True
    )

    class Meta:
        ordering = ('created',)
