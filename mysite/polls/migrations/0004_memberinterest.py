# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_interest'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interest', models.ForeignKey(to='polls.Interest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
