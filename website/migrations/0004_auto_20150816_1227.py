# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150802_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='default-synth', unique=True, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='synth',
            name='slug',
            field=models.SlugField(default='default-synth', unique=True, max_length=40),
            preserve_default=False,
        ),
    ]
