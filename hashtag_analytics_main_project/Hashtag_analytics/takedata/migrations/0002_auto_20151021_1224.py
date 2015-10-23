# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takedata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtags',
            name='postID',
        ),
        migrations.DeleteModel(
            name='hashtags',
        ),
        migrations.DeleteModel(
            name='postData',
        ),
    ]
