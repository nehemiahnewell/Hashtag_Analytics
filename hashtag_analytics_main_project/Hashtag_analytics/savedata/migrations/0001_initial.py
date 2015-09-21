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
                ('hashtag_found', models.CharField(max_length=140)),
                ('Use_By_Percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Use_By_Percentage_Posters', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='searchData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('hashtag_searched', models.CharField(max_length=140)),
                ('date_searched', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='hashtags',
            name='search',
            field=models.ForeignKey(to='savedata.searchData'),
        ),
    ]
