# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150816_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='synth',
            name='slug',
            field=models.SlugField(max_length=40, null=True, blank=True),
        ),
    ]
