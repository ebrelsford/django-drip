# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('drip', '0003_auto_20151109_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='querysetrule',
            name='drip',
        ),
        migrations.AddField(
            model_name='querysetrule',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='querysetrule',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
