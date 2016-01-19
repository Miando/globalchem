# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0003_auto_20160119_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='category',
        ),
        migrations.AddField(
            model_name='tovar',
            name='category',
            field=models.ManyToManyField(to='katalog.Category'),
        ),
    ]
