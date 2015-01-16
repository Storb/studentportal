# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_birthday', models.DateField(verbose_name='date birthday')),
                ('card_number', models.IntegerField(max_length=10)),
                ('group', models.ForeignKey(to='stud_db.Group', related_name='students')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='elder',
            field=models.OneToOneField(to='stud_db.Student', blank=True, null=True, related_name='group_elder', on_delete=django.db.models.deletion.SET_NULL),
            preserve_default=True,
        ),
    ]
