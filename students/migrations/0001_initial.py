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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name_model', models.CharField(max_length=20)),
                ('what_made', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=200, blank=True)),
                ('date_change', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('card_number', models.IntegerField(max_length=10)),
                ('date_birthday', models.DateField(verbose_name='date birthday')),
                ('group', models.ForeignKey(related_name='students', to='students.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='elder',
            field=models.ForeignKey(null=True, related_name='group_elder', blank=True, to='students.Student'),
            preserve_default=True,
        ),
    ]
