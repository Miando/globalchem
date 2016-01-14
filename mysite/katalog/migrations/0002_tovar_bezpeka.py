# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='bezpeka',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
