# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_text', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Synth',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('issue_year', models.DateField()),
                ('category', models.CharField(max_length=1, choices=[(b'mono', b'Monosynth'), (b'poly', b'Polysynth'), (b'dm', b'Drum machine')])),
                ('pic', models.ImageField(upload_to=b'synth_pics')),
                ('maker', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='synth',
            field=models.ForeignKey(to='website.Synth'),
        ),
    ]
