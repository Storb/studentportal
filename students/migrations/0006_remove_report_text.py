# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20141127_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='text',
        ),
    ]
