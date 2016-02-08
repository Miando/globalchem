# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_auto_20160120_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='bezpeka',
        ),
    ]
