# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0002_auto_20151109_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentdrip',
            old_name='content_type',
            new_name='drip_content_type',
        ),
        migrations.RenameField(
            model_name='sentdrip',
            old_name='object_id',
            new_name='drip_object_id',
        ),
    ]
