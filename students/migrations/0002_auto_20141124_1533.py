# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='elder',
            field=models.OneToOneField(to='students.Student', related_name='group_elder'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='students.Group', related_name='students', blank=True),
        ),
    ]
