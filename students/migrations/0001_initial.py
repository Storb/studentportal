# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('card_number', models.IntegerField(max_length=10)),
                ('date_birthday', models.DateField(verbose_name='date birthday')),
                ('group', models.ForeignKey(related_name='student', to='students.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='elder',
            field=models.ForeignKey(to='students.Student', blank=True, null=True, related_name='group_elder'),
            preserve_default=True,
        ),
    ]
