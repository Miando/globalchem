# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_auto_20160119_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tovar',
            old_name='text',
            new_name='opys',
        ),
        migrations.AddField(
            model_name='tovar',
            name='opublikovaty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tovar',
            name='zastosuvannya',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
