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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('hashtag_found', models.CharField(max_length=140)),
                ('Count', models.IntegerField()),
                ('Percentage', models.DecimalField(max_digits=4, decimal_places=2)),
                ('Posters', models.IntegerField()),
                ('Percentage_Posters', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='searchData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('hashtag_searched', models.CharField(max_length=140)),
                ('date_searched', models.DateTimeField(verbose_name='date published')),
                ('Tweets', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='hashtags',
            name='search',
            field=models.ForeignKey(to='savedata.searchData'),
        ),
    ]
