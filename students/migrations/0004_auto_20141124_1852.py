# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20141124_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='elder',
            field=models.OneToOneField(null=True, blank=True, related_name='group_elder', to='students.Student'),
        ),
    ]
