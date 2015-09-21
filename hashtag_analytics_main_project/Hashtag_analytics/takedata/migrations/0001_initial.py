# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hashtags',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('hashtag', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='postData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='hashtags',
            name='postID',
            field=models.ForeignKey(to='takedata.postData'),
        ),
    ]
