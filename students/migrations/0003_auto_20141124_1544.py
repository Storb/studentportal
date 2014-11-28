# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141124_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='elder',
            field=models.ForeignKey(to='students.Student', null=True, related_name='group_elder', blank=True),
        ),
    ]
