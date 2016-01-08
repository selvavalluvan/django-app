# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_memberinterest_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='areas_of_interest',
            field=models.ManyToManyField(to='polls.Interest'),
            preserve_default=True,
        ),
    ]
