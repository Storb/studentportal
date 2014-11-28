# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20141124_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='elder',
            field=models.OneToOneField(blank=True, related_name='group_elder', on_delete=django.db.models.deletion.SET_NULL, to='students.Student', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, related_name='students', to='students.Group', null=True),
        ),
    ]
