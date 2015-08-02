# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150802_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synth',
            name='category',
            field=models.CharField(max_length=5, choices=[(b'mono', b'Monosynth'), (b'poly', b'Polysynth'), (b'dm', b'Drum machine')]),
        ),
    ]
