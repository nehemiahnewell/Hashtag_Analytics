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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hashtag', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='postData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='hashtags',
            name='postID',
            field=models.ForeignKey(to='takedata.postData'),
        ),
    ]
