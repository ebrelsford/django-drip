# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('drip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentdrip',
            name='drip',
        ),
        migrations.AddField(
            model_name='sentdrip',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentdrip',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
